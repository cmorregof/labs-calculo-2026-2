#!/usr/bin/env python3
"""Construye el congelado mensual SIPSA-P 2013--2024 del Lab 2.

La fuente oficial publicada en datos.gov.co (conjunto gkqq-k3k5) es un
catálogo federado: sus ocho archivos ZIP anuales viven en Microdatos DANE.
Cada CSV usa nombres de columnas y formatos de fecha ligeramente distintos.
Este script los normaliza a fecha, ciudad, mercado, producto y precio_kg.

Uso:
    python3 congelar_sipsa.py [salida.csv.gz]
"""

from __future__ import annotations

import csv
import gzip
import io
import sys
import unicodedata
import urllib.request
import zipfile
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


FUENTES = {
    "2013-2017": "23898",
    "2018": "23897",
    "2019": "23896",
    "2020": "23895",
    "2021": "23894",
    "2022": "23893",
    "2023": "23892",
    "2024": "23891",
}
URL = "https://microdatos.dane.gov.co/index.php/catalog/776/download/{}"
MESES = {
    "ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6,
    "jul": 7, "ago": 8, "sep": 9, "oct": 10, "nov": 11, "dic": 12,
}


def sin_tildes(texto: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", texto.lower())
        if unicodedata.category(c) != "Mn"
    )


def fecha_normalizada(valor: str) -> str:
    """Convierte 1/01/2013 o ene-24 al formato AAAA-MM."""
    valor = valor.strip()
    if "/" in valor:
        return datetime.strptime(valor, "%d/%m/%Y").strftime("%Y-%m")
    mes, anio = valor.lower().split("-")
    return f"20{anio}-{MESES[mes]:02d}"


def precio_normalizado(valor: str) -> float:
    """Convierte separadores colombianos de miles a un número."""
    valor = valor.replace("\xa0", "").strip().replace(" ", "")
    if "," in valor and "." in valor:
        valor = valor.replace(".", "").replace(",", ".")
    elif "," in valor:
        valor = valor.replace(",", ".")
    elif "." in valor:
        entero, decimal = valor.rsplit(".", 1)
        if len(decimal) == 3:
            valor = entero.replace(".", "") + decimal
    return float(valor)


def ciudad_de_mercado(mercado: str) -> str:
    """Obtiene la ciudad antes de la primera coma del mercado reportado."""
    return mercado.split(",", 1)[0].strip()


def leer_csv_zip(contenido: bytes) -> list[dict[str, object]]:
    """Lee el CSV de un ZIP anual y devuelve filas del esquema del curso."""
    with zipfile.ZipFile(io.BytesIO(contenido)) as archivo:
        nombre = next(n for n in archivo.namelist() if n.lower().endswith(".csv"))
        bruto = archivo.read(nombre)

    try:
        texto = bruto.decode("utf-8-sig")
    except UnicodeDecodeError:
        texto = bruto.decode("latin-1")

    lector = csv.reader(io.StringIO(texto), delimiter=";")
    encabezado = next(lector)
    posiciones = {sin_tildes(nombre): i for i, nombre in enumerate(encabezado)}

    def posicion(*opciones: str) -> int:
        for opcion in opciones:
            if opcion in posiciones:
                return posiciones[opcion]
        raise ValueError(f"No encontré {opciones} en {encabezado}")

    i_fecha = posicion("fecha")
    i_producto = posicion("producto")
    i_mercado = posicion("mercado", "fuente")
    i_precio = next(i for nombre, i in posiciones.items() if nombre.startswith("precio"))

    filas = []
    for fila in lector:
        if not fila or len(fila) <= max(i_fecha, i_producto, i_mercado, i_precio):
            continue
        fecha = fecha_normalizada(fila[i_fecha])
        mercado = fila[i_mercado].strip()
        producto = fila[i_producto].strip()
        if not mercado or not producto:
            continue
        filas.append({
            "fecha": fecha,
            "ciudad": ciudad_de_mercado(mercado),
            "mercado": mercado,
            "producto": producto,
            "precio_kg": precio_normalizado(fila[i_precio]),
        })
    return filas


def descargar(identificador: str) -> bytes:
    solicitud = urllib.request.Request(
        URL.format(identificador), headers={"User-Agent": "labs-calculo-2026-2"}
    )
    with urllib.request.urlopen(solicitud, timeout=90) as respuesta:
        return respuesta.read()


def main() -> None:
    salida = Path(sys.argv[1] if len(sys.argv) > 1 else "sipsa_mensual.csv.gz")
    filas = []
    for etiqueta, identificador in FUENTES.items():
        print(f"Descargando {etiqueta}…", flush=True)
        filas.extend(leer_csv_zip(descargar(identificador)))

    # El archivo de 2021 repite ocho observaciones de tres enlatados. Para
    # conservar una sola observación por mes, mercado y producto, se promedia
    # ese precio repetido. La regla queda visible y es verificable.
    grupos = defaultdict(list)
    for fila in filas:
        grupos[(fila["fecha"], fila["mercado"], fila["producto"])].append(fila)
    duplicadas = sum(len(grupo) - 1 for grupo in grupos.values())
    if duplicadas:
        print(f"Promediando {duplicadas} filas repetidas de la fuente oficial.")
    filas = []
    for grupo in grupos.values():
        fila = dict(grupo[0])
        fila["precio_kg"] = round(
            sum(observacion["precio_kg"] for observacion in grupo) / len(grupo), 2
        )
        filas.append(fila)
    filas.sort(key=lambda fila: (fila["fecha"], fila["ciudad"], fila["mercado"], fila["producto"]))

    with gzip.open(salida, "wt", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(
            archivo, fieldnames=["fecha", "ciudad", "mercado", "producto", "precio_kg"]
        )
        escritor.writeheader()
        escritor.writerows(filas)

    meses = {fila["fecha"] for fila in filas}
    ciudades = {fila["ciudad"] for fila in filas}
    productos = {fila["producto"] for fila in filas}
    print(f"Escrito: {salida}")
    print(f"Filas: {len(filas)} | Meses: {min(meses)} a {max(meses)} ({len(meses)})")
    print(f"Ciudades: {len(ciudades)} | Productos: {len(productos)}")
    print("Filas por año:", dict(sorted(Counter(fila["fecha"][:4] for fila in filas).items())))


if __name__ == "__main__":
    main()
