# Datos del laboratorio L1 — *La factura de la ciudad*

| Archivo | Qué es | Fuente | Congelado |
|---|---|---|---|
| `londres_mensual.csv` | Consumo **mensual** por hogar de Londres (`hogar, mes, kwh`), 113 440 filas, 5 556 hogares, 2011-12 a 2014-02 | Producido con `agregar_londres.py` a partir de `london_energy.csv` | sept. 2026 |
| `london_energy.csv.gz` | Consumo **diario** por hogar (`LCLid, Date, KWH`), 3 510 433 filas, 5 566 hogares | Kaggle, *London Homes Energy Data* (emmanuelfwerr) — proyecto Low Carbon London, UK Power Networks | sept. 2026 |
| `chec_tarifas_congeladas.csv` | Pliego tarifario CHEC, 2008 a agosto de 2026 (40 294 filas) | datos.gov.co, dataset `c698-wqig` — *Costo unitario de tarifas de energía CHEC* | 28 sept. 2026 |
| `agregar_londres.py` | Script que produce el mensual a partir del diario (regla: meses con ≥ 25 días de lectura) | curso | — |

Huellas MD5 en `CHECKSUMS.md5`. Verificar: `md5sum -c CHECKSUMS.md5`.

Camino en vivo para el pliego (mismo formato que la copia congelada):
`https://www.datos.gov.co/resource/c698-wqig.csv?$limit=60000` — sin `$limit` la API devuelve solo 1 000 filas.
