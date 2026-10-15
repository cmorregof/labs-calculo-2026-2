#!/usr/bin/env python3
"""
congelar_arecibo.py — Descarga el mensaje de Arecibo (1974) de su fuente pública,
lo valida y lo congela en datos/arecibo.txt.

Introducción a las Ciencias de la Computación · UNAL Manizales · L1 Primer contacto.

Uso:
    python introduccion_cc/congelar_arecibo.py      # desde la raíz del repo: descarga y congela en datos/
    python introduccion_cc/congelar_arecibo.py --archivo crudo.txt   # usa un texto copiado a mano

Qué hace, paso a paso (esto es lo que hay que poder explicar):
  1. Trae el texto de la página "Arecibo message" de Wikipedia (o lee el archivo que le den).
  2. Busca bloques de renglones que solo tengan ceros y unos (ignorando espacios).
  3. Se queda con el bloque que tenga EXACTAMENTE 1679 bits. Si no hay uno, se detiene y avisa.
  4. Escribe datos/arecibo.txt: una sola línea de 1679 caracteres '0'/'1'.
  5. Imprime la huella del archivo: cuántos unos tiene y su SHA-256 (una "huella digital":
     si cambia un solo bit, la huella cambia por completo).
"""
import argparse
import hashlib
import html
import os
import re
import sys
import urllib.request

LONGITUD = 1679
FUENTES = [
    "https://en.wikipedia.org/w/index.php?title=Arecibo_message&action=raw",
    "https://en.wikipedia.org/wiki/Arecibo_message",
]


def descargar(url):
    pedido = urllib.request.Request(url, headers={"User-Agent": "UNAL-IntroCC-L1/1.0 (curso universitario)"})
    with urllib.request.urlopen(pedido, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def extraer_bits(texto):
    """CONTRATO. Recibe un texto cualquiera (wikitexto, HTML o lo que se copió a mano).
    Devuelve la cadena de 1679 caracteres '0'/'1' del mensaje, o None si no la encuentra.
    Supone que el mensaje aparece como renglones consecutivos hechos solo de 0 y 1."""
    # Caso 1: el mensaje viene como tabla HTML, una fila <tr> por renglón del mensaje
    if re.search(r"<tr\b", texto, flags=re.I):
        filas = []
        for trozo in re.split(r"<tr\b", texto, flags=re.I)[1:]:
            trozo = re.split(r"</tr>", trozo, flags=re.I)[0]
            filas.append(re.sub(r"\s", "", html.unescape(re.sub(r"<[^>]+>", "", "<" + trozo))))
        actual = []
        for f in filas + ["x"]:
            if f and set(f) <= {"0", "1"}:
                actual.append(f)
            else:
                if len("".join(actual)) == LONGITUD:
                    return "".join(actual)
                actual = []
    # Caso 2: el mensaje viene como renglones de texto (wikitexto, <pre>, o copiado a mano)
    texto = re.sub(r"<[^>]+>", "\n", texto)          # cada etiqueta HTML se vuelve salto de línea
    texto = html.unescape(texto)
    bloques, actual = [], []
    for renglon in texto.splitlines():
        limpio = re.sub(r"\s", "", renglon)
        if limpio == "":
            continue                                    # los renglones vacíos no cortan el bloque
        if set(limpio) <= {"0", "1"}:
            actual.append(limpio)
        else:
            if actual:
                bloques.append("".join(actual))
            actual = []
    if actual:
        bloques.append("".join(actual))
    for b in bloques:
        if len(b) == LONGITUD:
            return b
    return None


def huella(bits):
    """CONTRATO. Recibe la cadena de bits. Devuelve (número de unos, SHA-256 en hexadecimal)."""
    return bits.count("1"), hashlib.sha256(bits.encode("ascii")).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--archivo", help="texto copiado a mano de la página del mensaje")
    ap.add_argument("--salida", default=os.path.join("datos", "arecibo.txt"))
    a = ap.parse_args()

    bits = None
    if a.archivo:
        with open(a.archivo, encoding="utf-8") as f:
            bits = extraer_bits(f.read())
    else:
        for url in FUENTES:
            try:
                print("descargando", url)
                bits = extraer_bits(descargar(url))
            except Exception as e:                      # sin red, página cambiada, etc.
                print("  no se pudo:", e)
            if bits:
                break
    if not bits:
        sys.exit("No encontré un bloque de exactamente 1679 bits. Copien a mano la cuadrícula "
                 "de la página en un archivo y corran: python congelar_arecibo.py --archivo ese_archivo.txt")

    os.makedirs(os.path.dirname(a.salida) or ".", exist_ok=True)
    with open(a.salida, "w", encoding="ascii") as f:
        f.write(bits)
    unos, sha = huella(bits)
    print(f"\nCongelado en {a.salida}")
    print(f"  caracteres : {len(bits)}")
    print(f"  unos       : {unos}")
    print(f"  ceros      : {len(bits) - unos}")
    print(f"  SHA-256    : {sha}")
    print("\nCopien estas tres cifras en la sección 'Cifras de control' del README.")


if __name__ == "__main__":
    main()
