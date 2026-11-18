# D10 · La demanda de energía del país en la cuarentena

**Archivo:** `datos/D10_demanda_nacional_cuarentena_2020.csv` · 150 filas · 0 celdas vacías en la tasa

**Para cargarlo en Colab:** `https://raw.githubusercontent.com/cmorregof/labs-calculo-2026-2/main/integral/proyecto_final/datos/D10_demanda_nacional_cuarentena_2020.csv`

## Fuente
XM, operador del Sistema Interconectado Nacional. API pública `https://servapibi.xm.com.co`, métrica `DemaSIN` (demanda de energía del SIN).

Descargado el 18 de noviembre de 2026 con `scripts/construir_datos.py`.

## Periodo
25 de marzo a 21 de agosto de 2020, un dato por día.

## Qué mide
La energía que consumió el país cada día.

## Unidades
Tasa en GWh por día. El tiempo está en días.

## Columnas
| Columna | Qué es |
|---|---|
| `fecha` | fecha del dato |
| `t_dias` | tiempo desde el inicio de la ventana |
| `demanda_GWh_dia` | la tasa |

## Para tener en cuenta
La serie tiene un ciclo semanal marcado. El archivo no trae datos anteriores al 25 de marzo: si su línea base los necesita, `construir_datos.py` muestra cómo bajarlos. Las celdas vacías son datos que la fuente no reporta: no se rellenaron.

## La pregunta
¿Cuánta energía dejó de consumir el país durante la cuarentena? La línea base la definen y la defienden ustedes.

## Extensión optativa
EDO de variables separables. Si la demanda se recupera a un ritmo proporcional a lo que le falta para volver a su nivel, ¿qué ecuación cumple?
