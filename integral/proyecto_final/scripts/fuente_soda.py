"""Acceso mínimo a datos.gov.co (API Socrata/SODA). Devuelve DataFrames de pandas."""
import io, time
import pandas as pd
import requests

def soda(dataset_id, **consulta):
    url = f"https://www.datos.gov.co/resource/{dataset_id}.csv"
    for intento in range(4):
        try:
            r = requests.get(url, params=consulta, timeout=150)
            if r.status_code == 200:
                return pd.read_csv(io.StringIO(r.text))
        except requests.RequestException:
            pass
        time.sleep(3)
    raise RuntimeError(f"datos.gov.co no respondió: {dataset_id} {consulta}")

def ideam_rango(dataset_id, estacion, ini, fin, paso_dias=60):
    """Observaciones crudas de una estación IDEAM en [ini, fin), por tramos de fechas
    (la consulta con filtro de fechas responde en segundos; la agregada no)."""
    partes, a, fin = [], pd.Timestamp(ini), pd.Timestamp(fin)
    while a < fin:
        b = min(a + pd.Timedelta(days=paso_dias), fin)
        partes.append(soda(dataset_id, **{
            "$select": "fechaobservacion,valorobservado",
            "$where": f"codigoestacion='{estacion}' and fechaobservacion >= '{a.isoformat()}' "
                      f"and fechaobservacion < '{b.isoformat()}'",
            "$order": "fechaobservacion", "$limit": 50000}))
        a = b
    return pd.concat(partes, ignore_index=True)
