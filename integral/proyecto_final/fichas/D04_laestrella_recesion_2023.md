# D04 · Río La Estrella en temporada seca

**Archivo:** `datos/D04_laestrella_recesion_2023.csv` · 60 filas · 0 celdas vacías en la tasa

**Para cargarlo en Colab:** `https://raw.githubusercontent.com/cmorregof/labs-calculo-2026-2/main/integral/proyecto_final/datos/D04_laestrella_recesion_2023.csv`

## Fuente
XM, operador del Sistema Interconectado Nacional. API pública `https://servapibi.xm.com.co`, métrica `AporCaudal`, río `ESTRELLA` (región hidrológica Caldas).

Descargado el 18 de noviembre de 2026 con `scripts/construir_datos.py`.

## Periodo
27 de diciembre de 2023 a 24 de febrero de 2024, un dato por día.

## Qué mide
El caudal promedio diario del río.

## Unidades
Tasa en m³/s. El tiempo está en días.

## Columnas
| Columna | Qué es |
|---|---|
| `fecha` | fecha del dato |
| `t_dias` | tiempo desde el inicio de la ventana |
| `caudal_m3s` | la tasa |

## Para tener en cuenta
«Caudal base» no viene en los datos: lo definen ustedes. Las celdas vacías son datos que la fuente no reporta: no se rellenaron.

## La pregunta
En una temporada seca, ¿cuánta agua aportó el río en 60 días y qué parte de ella fue caudal base?

## Extensión optativa
EDO de variables separables, como en un tanque que se vacía a un ritmo proporcional a lo que le queda.
