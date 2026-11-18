# D05 · COVID-19 en Manizales: la ola de ómicron

**Archivo:** `datos/D05_covid_omicron_manizales.csv` · 84 filas · 0 celdas vacías en la tasa

**Para cargarlo en Colab:** `https://raw.githubusercontent.com/cmorregof/labs-calculo-2026-2/main/integral/proyecto_final/datos/D05_covid_omicron_manizales.csv`

## Fuente
Instituto Nacional de Salud, conjunto «Casos positivos de COVID-19 en Colombia» (`gt2j-8ykr`) en datos.gov.co. Se filtró el municipio 17001 y se contó un caso por fila según su fecha de notificación.

Descargado el 18 de noviembre de 2026 con `scripts/construir_datos.py`.

## Periodo
13 de diciembre de 2021 a 6 de marzo de 2022, un dato por día.

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
Los fines de semana se notifican menos casos. Eso es del sistema de notificación, no de la enfermedad. Las celdas vacías son datos que la fuente no reporta: no se rellenaron.

## La pregunta
¿Cuántos casos dejó la ola de ómicron en la ciudad y qué fracción se notificó antes del pico?

## Extensión optativa
Serie geométrica. Si su modelo tiene la forma A/(1+u²), escriban 1/(1+u²) como serie geométrica, intégrenla término a término cerca del pico y acoten el error.
