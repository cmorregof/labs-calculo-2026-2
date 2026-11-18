# D03 · El trasvase del Guarinó

**Archivo:** `datos/D03_guarino_trasvase_2024.csv` · 90 filas · 0 celdas vacías en la tasa

**Para cargarlo en Colab:** `https://raw.githubusercontent.com/cmorregof/labs-calculo-2026-2/main/integral/proyecto_final/datos/D03_guarino_trasvase_2024.csv`

## Fuente
XM, operador del Sistema Interconectado Nacional. API pública `https://servapibi.xm.com.co`, métrica `AporCaudal`, serie `DESV. GUARINO`.

Descargado el 18 de noviembre de 2026 con `scripts/construir_datos.py`.

## Periodo
6 de julio a 3 de octubre de 2024, un dato por día.

## Qué mide
El caudal diario que el trasvase desvía del río Guarinó hacia el embalse Amaní. El trasvase opera desde 2010.

## Unidades
Tasa en m³/s. El tiempo está en días.

## Columnas
| Columna | Qué es |
|---|---|
| `fecha` | fecha del dato |
| `t_dias` | tiempo desde el inicio de la ventana |
| `caudal_m3s` | la tasa |

## Para tener en cuenta
Hay días con caudal muy cercano a cero. Son datos, no vacíos. Las celdas vacías son datos que la fuente no reporta: no se rellenaron.

## La pregunta
¿Cuánta agua del Guarinó pasó hacia el embalse en esos 90 días, y en qué día iba la mitad?

## Extensión optativa
Esperanza. Con el caudal leído como densidad, ¿cuál es el día promedio de llegada del agua? ¿Existe esa integral si el modelo se extiende a todo t ≥ 0?
