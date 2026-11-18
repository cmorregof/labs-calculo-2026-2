# D07 · La demanda de energía de CHEC en una semana

**Archivo:** `datos/D07_demanda_chec_semana.csv` · 168 filas · 0 celdas vacías en la tasa

**Para cargarlo en Colab:** `https://raw.githubusercontent.com/cmorregof/labs-calculo-2026-2/main/integral/proyecto_final/datos/D07_demanda_chec_semana.csv`

## Fuente
XM, operador del Sistema Interconectado Nacional. API pública `https://servapibi.xm.com.co`, métrica `DemaReal` (demanda real por agente), agente `CHCC` (CHEC como comercializador).

Descargado el 18 de noviembre de 2026 con `scripts/construir_datos.py`.

## Periodo
Lunes 10 a domingo 16 de marzo de 2025, un dato por hora.

## Qué mide
La energía demandada en cada hora, expresada como potencia promedio de esa hora.

## Unidades
Tasa en MW. El tiempo está en horas.

## Columnas
| Columna | Qué es |
|---|---|
| `fecha_hora` | fecha del dato |
| `t_horas` | tiempo desde el inicio de la ventana |
| `demanda_MW` | la tasa |

## Para tener en cuenta
XM publica kWh por hora; aquí se dividió entre 1000 para dejarlo en MW. El fin de semana no se parece a los días hábiles. Las celdas vacías son datos que la fuente no reporta: no se rellenaron.

## La pregunta
¿Cuánta energía consumieron los usuarios de CHEC en esa semana, y cuánta de ella está por encima del consumo mínimo de la madrugada?

## Extensión optativa
No tiene.
