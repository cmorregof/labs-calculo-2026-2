#!/usr/bin/env python3
"""Proyecto final de Cálculo Integral 2026-II (UNAL Manizales).
Genera, desde las fuentes públicas, los CSV del menú de datos.

Uso:   python construir_datos.py            (todos)
       python construir_datos.py D05 D08    (solo algunos)

Cada CSV tiene tres columnas: fecha (o fecha y hora), t (tiempo desde el inicio
de la ventana, en la unidad que dice la ficha) y la tasa. Las celdas vacías son
datos que la fuente no reporta: no se rellenan aquí. Esa decisión es del grupo.

Fuentes: XM (API pública servapibi.xm.com.co), datos.gov.co (INS e IDEAM),
Federación Nacional de Cafeteros y Our World in Data (Global Carbon Project). Requiere: pandas, requests, openpyxl.
"""
import io, os, sys
import numpy as np
import pandas as pd
import requests
import fuente_xm as xm
from fuente_soda import soda, ideam_rango

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, "..", "datos")
os.makedirs(SALIDA, exist_ok=True)

def guardar(df, nombre):
    ruta = os.path.join(SALIDA, nombre + ".csv")
    df.to_csv(ruta, index=False, float_format="%.6g")
    print(f"{nombre}: {len(df)} filas, {int(df.iloc[:, -1].isna().sum())} vacías -> {ruta}")

# ---------------------------------------------------------------- XM: caudales
def caudal(rio, inicio, dias, nombre):
    """Aporte diario de un río del SIN (métrica AporCaudal, m3/s, promedio del día)."""
    ini = pd.Timestamp(inicio); fin = ini + pd.Timedelta(days=dias - 1)
    d = xm.diario("AporCaudal", "Rio", ini, fin)
    d = d[d.nombre == rio].copy()
    d["fecha"] = pd.to_datetime(d.fecha)
    s = d.set_index("fecha").valor.reindex(pd.date_range(ini, fin, freq="D"))
    out = pd.DataFrame({"fecha": s.index.date, "t_dias": np.arange(len(s)), "caudal_m3s": s.values})
    guardar(out, nombre)

def D01(): caudal("CHINCHINA", "2026-04-25", 90, "D01_chinchina_creciente_2026")
def D02(): caudal("MIEL I", "2022-04-03", 60, "D02_lamiel_recesion_2022")
def D03(): caudal("DESV. GUARINO", "2024-07-06", 90, "D03_guarino_trasvase_2024")
def D04(): caudal("ESTRELLA", "2023-12-27", 60, "D04_laestrella_recesion_2023")
def R1():  caudal("SAN FRANCISCO", "2025-06-09", 60, "R1_sanfrancisco_recesion_2025")
def R2():  caudal("CAMPOALEGRE", "2023-05-18", 90, "R2_campoalegre_creciente_2023")

# ---------------------------------------------------------------- INS: covid
def covid(inicio, fin, nombre):
    """Casos positivos de COVID-19 notificados por día en Manizales (DIVIPOLA 17001).
    Conjunto gt2j-8ykr del INS en datos.gov.co; un caso por fila, se cuenta por fecha de notificación."""
    cache = os.path.join(AQUI, "_cache_covid_manizales.csv")
    if not os.path.exists(cache):     # la consulta agregada tarda cerca de un minuto
        soda("gt2j-8ykr", **{"$select": "fecha_de_notificaci_n,count(*) as n", "$where": "ciudad_municipio='17001'",
                             "$group": "fecha_de_notificaci_n", "$limit": 50000}).to_csv(cache, index=False)
    c = pd.read_csv(cache)
    c["f"] = pd.to_datetime(c.fecha_de_notificaci_n).dt.normalize()
    s = c.groupby("f").n.sum().reindex(pd.date_range(inicio, fin, freq="D"))
    out = pd.DataFrame({"fecha": s.index.date, "t_dias": np.arange(len(s)), "casos_por_dia": s.values})
    guardar(out, nombre)

def D05(): covid("2021-12-13", "2022-03-06", "D05_covid_omicron_manizales")
def D06(): covid("2020-07-06", "2020-12-06", "D06_covid_primera_ola_manizales")

# ---------------------------------------------------------------- XM: horarias
def horaria(metric, entidad, codigo, inicio, fin, columna, nombre):
    """Serie horaria de XM en kWh por hora; se entrega en MW (energía de la hora / 1 h / 1000)."""
    h = xm.horario(metric, entidad, inicio, fin, [codigo])
    h["fh"] = pd.to_datetime(h.fecha) + pd.to_timedelta(h.hora, unit="h")
    s = h.set_index("fh").valor.reindex(pd.date_range(inicio, pd.Timestamp(fin) + pd.Timedelta(hours=23), freq="h"))
    out = pd.DataFrame({"fecha_hora": s.index.strftime("%Y-%m-%d %H:%M"), "t_horas": np.arange(len(s)),
                        columna: (s.values / 1000.0)})
    guardar(out, nombre)

def D07(): horaria("DemaReal", "Agente", "CHCC", "2025-03-10", "2025-03-16", "demanda_MW", "D07_demanda_chec_semana")
def D08(): horaria("Gene", "Recurso", "TPUY", "2025-09-19", "2025-09-23", "potencia_MW", "D08_tepuy_solar_5dias")

# ---------------------------------------------------------------- FNC: café
URL_FNC = ("https://federaciondecafeteros.org/wp-content/uploads/2026/09/"
           "Precios-area-y-produccion-de-cafe-Noviembre-2026-1.xlsx")
def D09():
    """Producción registrada mensual de café de Colombia (miles de sacos de 60 kg por mes)."""
    r = requests.get(URL_FNC, timeout=120); r.raise_for_status()
    x = pd.read_excel(io.BytesIO(r.content), sheet_name="8. Producción mensual", header=None).iloc[6:, [3, 4]]
    x.columns = ["mes", "prod"]
    x["mes"] = pd.to_datetime(x.mes, errors="coerce"); x["prod"] = pd.to_numeric(x["prod"], errors="coerce")
    s = x.dropna(subset=["mes"]).set_index("mes")["prod"].reindex(pd.date_range("2018-01-01", "2025-12-01", freq="MS"))
    out = pd.DataFrame({"mes": s.index.strftime("%Y-%m"), "t_meses": np.arange(len(s)),
                        "dias_del_mes": s.index.days_in_month, "produccion_miles_sacos_mes": s.values})
    out = out[["mes", "t_meses", "dias_del_mes", "produccion_miles_sacos_mes"]]
    guardar(out, "D09_cafe_produccion_mensual")

# ---------------------------------------------------------------- IDEAM
NUBIA = "0026155110"   # Aeropuerto La Nubia, Manizales (automática)
def D12():
    """Velocidad del viento en La Nubia, una semana, promedio de cada hora (m/s).
    La estación reporta cada 10 minutos; una hora con menos de 4 lecturas se deja vacía."""
    w = ideam_rango("sgfv-3yp8", NUBIA, "2023-01-23", "2023-01-30")
    w["f"] = pd.to_datetime(w.fechaobservacion)
    h = w.set_index("f").valorobservado.resample("h").agg(["mean", "count"])
    h = h.reindex(pd.date_range("2023-01-23", "2023-01-29 23:00", freq="h"))
    v = h["mean"].where(h["count"] >= 4)
    out = pd.DataFrame({"fecha_hora": h.index.strftime("%Y-%m-%d %H:%M"), "t_horas": np.arange(len(h)),
                        "lecturas_de_la_hora": h["count"].fillna(0).astype(int).values, "viento_m_s": v.values})
    guardar(out, "D12_viento_lanubia_semana")

# ---------------------------------------------------------------- XM: demanda nacional
def D10():
    """Demanda diaria de energía del SIN (métrica DemaSIN, kWh por día) en la cuarentena de 2020, en GWh/día."""
    d = xm.diario("DemaSIN", "Sistema", "2020-03-25", "2020-08-21")
    d["fecha"] = pd.to_datetime(d.fecha)
    s = pd.to_numeric(d.set_index("fecha").valor, errors="coerce").reindex(pd.date_range("2020-03-25", "2020-08-21"))
    out = pd.DataFrame({"fecha": s.index.date, "t_dias": np.arange(len(s)), "demanda_GWh_dia": s.values / 1e6})
    guardar(out, "D10_demanda_nacional_cuarentena_2020")

# ---------------------------------------------------------------- OWID / Global Carbon Project
def D11():
    """Emisiones anuales de CO2 de Colombia por combustibles fósiles e industria (Mt de CO2 por año), 1950 en adelante."""
    r = requests.get("https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv", timeout=180); r.raise_for_status()
    o = pd.read_csv(io.StringIO(r.text), usecols=["country", "year", "co2"])
    o = o[(o.country == "Colombia") & (o.year >= 1950)].sort_values("year")
    out = pd.DataFrame({"anio": o.year.values, "t_anios": o.year.values - 1950, "emisiones_MtCO2_anio": o.co2.values})
    guardar(out, "D11_co2_colombia_anual")

FUNCIONES = {f.__name__: f for f in [D01, D02, D03, D04, D05, D06, D07, D08, D09, D10, D11, D12, R1, R2]}
if __name__ == "__main__":
    pedir = sys.argv[1:] or list(FUNCIONES)
    for k in pedir:
        try:
            FUNCIONES[k]()
        except Exception as e:          # una fuente caída no detiene a las demás
            print(f"{k}: FALLÓ ({type(e).__name__}: {e})")
