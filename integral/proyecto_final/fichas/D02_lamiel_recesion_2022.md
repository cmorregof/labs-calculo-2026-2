# D02 · Río La Miel: el caudal que baja

**Archivo:** `datos/D02_lamiel_recesion_2022.csv` · 60 filas · 0 celdas vacías en la tasa

**Para cargarlo en Colab:** `https://raw.githubusercontent.com/cmorregof/labs-calculo-2026-2/main/integral/proyecto_final/datos/D02_lamiel_recesion_2022.csv`

## Fuente
XM, operador del Sistema Interconectado Nacional. API pública `https://servapibi.xm.com.co`, métrica `AporCaudal`, río `MIEL I`.

Descargado el 18 de noviembre de 2026 con `scripts/construir_datos.py`.

## Periodo
3 de abril a 1 de junio de 2022, un dato por día.

## Qué mide
El caudal promedio diario del río La Miel, que alimenta el embalse Amaní de la central Miel I (Norcasia, Caldas).

## Unidades
Tasa en m³/s. El tiempo está en días.

## Columnas
| Columna | Qué es |
|---|---|
| `fecha` | fecha del dato |
| `t_dias` | tiempo desde el inicio de la ventana |
| `caudal_m3s` | la tasa |

## Para tener en cuenta
El caudal no baja de forma pareja: hay días de lluvia en medio. Las celdas vacías son datos que la fuente no reporta: no se rellenaron.

## La pregunta
¿Cuánta agua le entregó el río al embalse Amaní mientras su caudal bajaba, y cuánta de ella llegó en los primeros veinte días?

## Extensión optativa
EDO de variables separables. Si el caudal baja a un ritmo proporcional a lo que le falta para llegar a un caudal base, ¿qué ecuación cumple y cuál es su solución?
