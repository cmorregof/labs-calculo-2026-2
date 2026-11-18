# D01 · Río Chinchiná: una creciente

**Archivo:** `datos/D01_chinchina_creciente_2026.csv` · 90 filas · 0 celdas vacías en la tasa

**Para cargarlo en Colab:** `https://raw.githubusercontent.com/cmorregof/labs-calculo-2026-2/main/integral/proyecto_final/datos/D01_chinchina_creciente_2026.csv`

## Fuente
XM, operador del Sistema Interconectado Nacional. API pública `https://servapibi.xm.com.co`, métrica `AporCaudal` (aportes de caudal por río), río `CHINCHINA`.

Descargado el 18 de noviembre de 2026 con `scripts/construir_datos.py`.

## Periodo
25 de abril a 23 de julio de 2026, un dato por día.

## Qué mide
El caudal promedio de cada día, en metros cúbicos por segundo.

## Unidades
Tasa en m³/s. El tiempo está en días. Antes de acumular hay que poner las dos cosas en la misma unidad de tiempo.

## Columnas
| Columna | Qué es |
|---|---|
| `fecha` | fecha del dato |
| `t_dias` | tiempo desde el inicio de la ventana |
| `caudal_m3s` | la tasa |

## Para tener en cuenta
«El caudal que el río ya traía» no está definido en los datos: lo definen ustedes. Las celdas vacías son datos que la fuente no reporta: no se rellenaron.

## La pregunta
¿Cuánta agua bajó por el río en esos 90 días, y cuánta de ella la trajo la creciente por encima del caudal que el río ya traía?

## Extensión optativa
Esperanza. Si se lee el exceso de caudal como una densidad en el tiempo, ¿en qué día llega, en promedio, el agua de la creciente?
