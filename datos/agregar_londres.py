#!/usr/bin/env python3
"""
Congela el dataset del Lab 1: agrega los consumos diarios de Londres a consumo
mensual por hogar -> londres_mensual.csv (columnas: hogar, mes, kwh).

Acepta cualquiera de los dos archivos de Kaggle:
  - london_energy.csv  (emmanuelfwerr: LCLid, Date, KWH)
  - daily_dataset.csv  (jeanmidev:     LCLid, day, energy_sum)

Uso:  python3 agregar_londres.py <archivo_descargado.csv>
"""
import sys
import pandas as pd

entrada = sys.argv[1] if len(sys.argv) > 1 else "london_energy.csv"
df = pd.read_csv(entrada)

# Normalizar nombres segun la variante descargada
cols = {c.lower(): c for c in df.columns}
col_id = cols.get("lclid")
col_fecha = cols.get("date") or cols.get("day")
col_kwh = cols.get("kwh") or cols.get("energy_sum")
if not (col_id and col_fecha and col_kwh):
    sys.exit(f"Columnas no reconocidas: {list(df.columns)}")

df = df.rename(columns={col_id: "hogar", col_fecha: "fecha", col_kwh: "kwh_dia"})
df["kwh_dia"] = pd.to_numeric(df["kwh_dia"], errors="coerce")
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
df = df.dropna(subset=["fecha"])
df["mes"] = df["fecha"].dt.strftime("%Y-%m")

# Agregar: suma mensual + cobertura (dias con lectura en el mes)
g = df.groupby(["hogar", "mes"]).agg(kwh=("kwh_dia", "sum"),
                                     dias=("kwh_dia", "count")).reset_index()

# Higiene documentada: solo meses con cobertura casi completa (>=25 dias con lectura),
# para que un "mes" signifique de verdad un mes. Decision registrada aqui.
antes = len(g)
g = g[g["dias"] >= 25].drop(columns="dias")
g["kwh"] = g["kwh"].round(2)

g = g.sort_values(["hogar", "mes"])
g.to_csv("londres_mensual.csv", index=False)

print(f"Hogares: {g['hogar'].nunique()} | Filas: {len(g)} (descartadas por mes incompleto: {antes - len(g)})")
print(f"Rango: {g['mes'].min()} a {g['mes'].max()} | Mediana kWh/mes: {g['kwh'].median():.1f}")
print("Escrito: londres_mensual.csv")
