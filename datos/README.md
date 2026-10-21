# Datos de los laboratorios

| Archivo | Qué es | Fuente | Congelado |
|---|---|---|---|
| `londres_mensual.csv` | Consumo **mensual** por hogar de Londres (`hogar, mes, kwh`), 113 440 filas, 5 556 hogares, 2011-12 a 2014-02 | Producido con `agregar_londres.py` a partir de `london_energy.csv` | sept. 2026 |
| `london_energy.csv.gz` | Consumo **diario** por hogar (`LCLid, Date, KWH`), 3 510 433 filas, 5 566 hogares | Kaggle, *London Homes Energy Data* (emmanuelfwerr) — proyecto Low Carbon London, UK Power Networks | sept. 2026 |
| `chec_tarifas_congeladas.csv` | Pliego tarifario CHEC, 2008 a agosto de 2026 (40 294 filas) | datos.gov.co, dataset `c698-wqig` — *Costo unitario de tarifas de energía CHEC* | 28 sept. 2026 |
| `agregar_londres.py` | Script que produce el mensual a partir del diario (regla: meses con ≥ 25 días de lectura) | curso | — |
| `arecibo.txt` | Mensaje de Arecibo (16 nov. 1974): una línea de 1 679 caracteres `0`/`1` (397 unos). Lo usa Introducción a las CC, L1 *Primer contacto* | Wikipedia, *Arecibo message*, con `introduccion_cc/congelar_arecibo.py` | oct. 2026 |
| `momentum_final2022.csv` | Tasa de dominio de la final del Mundial 2022 (Argentina–Francia), minuto corrido a minuto: `minuto, peligro_arg, peligro_fra, momentum_bruto, momentum`, 142 filas. Lo usa Integral, L2 *El partido que se acumula* | Producido con `preparar_momentum.py` a partir del evento a evento | oct. 2026 |
| `eventos_final2022.csv` | Evento a evento simplificado de la misma final (`periodo, minuto, segundo, t_corrido, equipo, tipo, x, y, xg, gol, peligro`), 4 386 filas, penales excluidos | StatsBomb Open Data, partido 3869685 | oct. 2026 |
| `preparar_momentum.py` | Script que descarga el evento a evento de StatsBomb y produce los dos CSV anteriores con la receta del curso (pesos, zona de peligro, memoria τ = 3 min). Sirve para cualquier partido: `--partido`, `--match-id`, `--listar` | curso | — |

Huellas MD5 en `CHECKSUMS.md5`. Verificar: `md5sum -c CHECKSUMS.md5`.

Camino en vivo para el pliego (mismo formato que la copia congelada):
`https://www.datos.gov.co/resource/c698-wqig.csv?$limit=60000` — sin `$limit` la API devuelve solo 1 000 filas.
