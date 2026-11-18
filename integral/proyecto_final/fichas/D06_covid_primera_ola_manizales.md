# D06 · COVID-19 en Manizales: la primera ola

**Archivo:** `datos/D06_covid_primera_ola_manizales.csv` · 154 filas · 0 celdas vacías en la tasa

**Para cargarlo en Colab:** `https://raw.githubusercontent.com/cmorregof/labs-calculo-2026-2/main/integral/proyecto_final/datos/D06_covid_primera_ola_manizales.csv`

## Fuente
Instituto Nacional de Salud, conjunto `gt2j-8ykr` en datos.gov.co, municipio 17001, conteo por fecha de notificación.

Descargado el 18 de noviembre de 2026 con `scripts/construir_datos.py`.

## Periodo
6 de julio a 6 de diciembre de 2020, un dato por día.

## Qué mide
El número de casos notificados cada día en Manizales.

## Unidades
Tasa en casos por día. El tiempo está en días.

## Columnas
| Columna | Qué es |
|---|---|
| `fecha` | fecha del dato |
| `t_dias` | tiempo desde el inicio de la ventana |
| `casos_por_dia` | la tasa |

## Para tener en cuenta
Los primeros dos tercios de la ventana terminan antes del pico. Piensen si con ese tramo el modelo alcanza a ver la forma de la ola. Las celdas vacías son datos que la fuente no reporta: no se rellenaron.

## La pregunta
¿Cuántos casos acumuló la primera ola y en qué fecha iba por la mitad?

## Extensión optativa
EDO de variables separables. Si los casos acumulados C(t) crecen según C' = kC(M − C), resuélvanla con fracciones parciales y comparen con sus datos.
