# D11 · Las emisiones de CO₂ de Colombia

**Archivo:** `datos/D11_co2_colombia_anual.csv` · 76 filas · 0 celdas vacías en la tasa

**Para cargarlo en Colab:** `https://raw.githubusercontent.com/cmorregof/labs-calculo-2026-2/main/integral/proyecto_final/datos/D11_co2_colombia_anual.csv`

## Fuente
Global Carbon Project, publicado por Our World in Data. Archivo `owid-co2-data.csv` del repositorio `owid/co2-data`, columna `co2`, país Colombia.

Descargado el 18 de noviembre de 2026 con `scripts/construir_datos.py`.

## Periodo
1950 a 2025, un dato por año.

## Qué mide
Las emisiones anuales de CO₂ por combustibles fósiles e industria. No incluye el cambio de uso del suelo.

## Unidades
Tasa en millones de toneladas de CO₂ por año. El tiempo está en años.

## Columnas
| Columna | Qué es |
|---|---|
| `anio` | fecha del dato |
| `t_anios` | tiempo desde el inicio de la ventana |
| `emisiones_MtCO2_anio` | la tasa |

## Para tener en cuenta
Los años más recientes de esta fuente son estimaciones preliminares. Las celdas vacías son datos que la fuente no reporta: no se rellenaron.

## La pregunta
¿Cuánto CO₂ ha emitido el país desde 1950 y en qué año había emitido la mitad?

## Extensión optativa
EDO de variables separables. Si las emisiones crecen a un ritmo proporcional a sí mismas, ¿qué predice el modelo y hasta dónde es creíble?
