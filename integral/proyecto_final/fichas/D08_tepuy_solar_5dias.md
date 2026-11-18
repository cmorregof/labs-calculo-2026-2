# D08 · El parque solar Tepuy en cinco días

**Archivo:** `datos/D08_tepuy_solar_5dias.csv` · 120 filas · 59 celdas vacías en la tasa

**Para cargarlo en Colab:** `https://raw.githubusercontent.com/cmorregof/labs-calculo-2026-2/main/integral/proyecto_final/datos/D08_tepuy_solar_5dias.csv`

## Fuente
XM, operador del Sistema Interconectado Nacional. API pública `https://servapibi.xm.com.co`, métrica `Gene` (generación por recurso), recurso `TPUY`.

Descargado el 18 de noviembre de 2026 con `scripts/construir_datos.py`.

## Periodo
19 a 23 de septiembre de 2025, un dato por hora.

## Qué mide
La potencia promedio que el parque solar Tepuy (La Dorada, Caldas; 83 MW nominales) entregó en cada hora.

## Unidades
Tasa en MW. El tiempo está en horas.

## Columnas
| Columna | Qué es |
|---|---|
| `fecha_hora` | fecha del dato |
| `t_horas` | tiempo desde el inicio de la ventana |
| `potencia_MW` | la tasa |

## Para tener en cuenta
Casi la mitad de las celdas están vacías: XM no reporta las horas en que el parque no genera. Qué valor tienen esas horas lo deciden ustedes. Las celdas vacías son datos que la fuente no reporta: no se rellenaron.

## La pregunta
¿Cuánta energía entregó el parque en esos cinco días, y cuánta dejó de entregar frente a cinco días como el mejor de la ventana?

## Extensión optativa
No tiene.
