# D09 · La producción de café de Colombia

**Archivo:** `datos/D09_cafe_produccion_mensual.csv` · 96 filas · 0 celdas vacías en la tasa

**Para cargarlo en Colab:** `https://raw.githubusercontent.com/cmorregof/labs-calculo-2026-2/main/integral/proyecto_final/datos/D09_cafe_produccion_mensual.csv`

## Fuente
Federación Nacional de Cafeteros, estadísticas cafeteras, archivo «Precios, área y producción de café», hoja «8. Producción mensual». `https://federaciondecafeteros.org/estadisticas-cafeteras/`

Descargado el 18 de noviembre de 2026 con `scripts/construir_datos.py`.

## Periodo
Enero de 2018 a diciembre de 2025, un dato por mes.

## Qué mide
La producción registrada de cada mes, en miles de sacos de 60 kg de café verde.

## Unidades
Tasa en miles de sacos por mes. El tiempo está en meses.

## Columnas
| Columna | Qué es |
|---|---|
| `mes` | fecha del dato |
| `t_meses` | tiempo desde el inicio de la ventana |
| `dias_del_mes` | columna de apoyo, ver la nota |
| `produccion_miles_sacos_mes` | la tasa |

## Para tener en cuenta
Los meses no duran lo mismo. La columna `dias_del_mes` está para que decidan si eso importa. Las celdas vacías son datos que la fuente no reporta: no se rellenaron.

## La pregunta
¿Cuántos sacos produjo el país en esos ocho años y qué parte se recoge en el último trimestre de cada año?

## Extensión optativa
No tiene.
