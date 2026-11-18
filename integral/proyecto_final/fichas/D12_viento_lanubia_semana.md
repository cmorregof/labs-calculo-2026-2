# D12 · El viento en La Nubia

**Archivo:** `datos/D12_viento_lanubia_semana.csv` · 168 filas · 2 celdas vacías en la tasa

**Para cargarlo en Colab:** `https://raw.githubusercontent.com/cmorregof/labs-calculo-2026-2/main/integral/proyecto_final/datos/D12_viento_lanubia_semana.csv`

## Fuente
IDEAM, conjunto «Velocidad del viento» (`sgfv-3yp8`) en datos.gov.co, estación Aeropuerto La Nubia (código 0026155110), Manizales.

Descargado el 18 de noviembre de 2026 con `scripts/construir_datos.py`.

## Periodo
23 a 29 de enero de 2023, un dato por hora.

## Qué mide
La velocidad del viento promedio de cada hora. La estación reporta cada 10 minutos; aquí se promedió por hora.

## Unidades
Tasa en m/s. El tiempo está en horas. Lo acumulado es una distancia: el recorrido del viento.

## Columnas
| Columna | Qué es |
|---|---|
| `fecha_hora` | fecha del dato |
| `t_horas` | tiempo desde el inicio de la ventana |
| `lecturas_de_la_hora` | columna de apoyo, ver la nota |
| `viento_m_s` | la tasa |

## Para tener en cuenta
Una hora con menos de 4 de sus 6 lecturas quedó vacía. La columna `lecturas_de_la_hora` dice cuántas hubo. La fuente no documenta si la hora es local o UTC. Las celdas vacías son datos que la fuente no reporta: no se rellenaron.

## La pregunta
¿Cuál fue el recorrido del viento en esa semana, en kilómetros, y qué fracción ocurre en las seis horas de más viento de cada día?

## Extensión optativa
No tiene.
