# Laboratorios computacionales — Cálculo Diferencial · Cálculo Integral · Introducción a las Ciencias de la Computación

Universidad Nacional de Colombia, Sede Manizales · 2026-II

Los tres cursos comparten la misma infraestructura de laboratorio: cuadernos en **Google Colab**, datos congelados en este repositorio, una cuenta de **Kaggle** para ir a la fuente, y una IA que trabaja de tutora, no de autora. Nada que instalar: todo corre en el navegador.

## Empezar aquí

1. Lee la **[Guía Sesión 0](sesion0/Guia_Sesion_0_Antes_del_primer_laboratorio.pdf)**: cuentas, descargas, glosario y la prueba de humo.
2. Abre el cuaderno de tu curso en Colab (enlaces de abajo), guarda tu copia en Drive y trabaja sobre ella.

| Curso | Guía | Cuaderno sesión 1 | Cuaderno sesión 2 |
|---|---|---|---|
| Cálculo Diferencial | [Guía L1](diferencial/Guia_L1_La_factura_de_la_ciudad.pdf) | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/diferencial/L1_sesion1.ipynb) | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/diferencial/L1_sesion2.ipynb) |
| Cálculo Diferencial — **L2** | [Guía L2 · El índice sancocho](diferencial/Guia_L2_El_indice_sancocho.pdf) | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/diferencial/L2_sesion1.ipynb) | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/diferencial/L2_sesion2.ipynb) |
| Cálculo Integral | [Guía L1](integral/Guia_L1_La_factura_de_la_ciudad.pdf) · [gráfica P1](integral/prediccion_P1_enero2013.pdf) | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/integral/L1_sesion1.ipynb) | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/integral/L1_sesion2.ipynb) |
| Cálculo Integral — **L2** | [Guía L2 · El partido que se acumula](integral/Guia_L2_El_partido_que_se_acumula.pdf) · [gráfica P1](integral/prediccion_P1_momentum_final2022.pdf) | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/integral/L2_sesion1.ipynb) | próximamente |
| Introducción a las CC | [Guía L1 · Primer contacto](introduccion_cc/Guia_L1_Primer_contacto.pdf) · [tarea puente](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/introduccion_cc/L1_tarea_puente.ipynb) | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/introduccion_cc/L1_sesion1.ipynb) | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/introduccion_cc/L1_sesion2.ipynb) |

## Datos

Todo en [`datos/`](datos/README.md), con huellas MD5. El L2 de Integral usa el evento a evento de la final del Mundial 2022 (StatsBomb Open Data); `preparar_momentum.py` lo reproduce desde la fuente. El crudo de Kaggle (`london_energy.csv`, 96 MB) **no** está aquí a propósito: descargarlo de la fuente es la tarea puente.

## Protocolo de IA

Intento propio antes de consultar · la IA no es la autoridad final · todo uso va a la bitácora individual. Detalles en la Guía Sesión 0.

## Estructura

```
sesion0/           Guía común a los tres cursos (fuente .tex y PDF)
diferencial/       L1 La factura de la ciudad + L2 El índice sancocho, con guías y cuadernos de ambas sesiones
integral/          L1: guía + gráfica de predicción + cuadernos sesiones 1 y 2 · L2: guía + gráfica de predicción + cuaderno sesión 1
introduccion_cc/   L1 Primer contacto: guía + cuadernos sesión 1, tarea puente y sesión 2 (la factura, archivada en factura_sesion1/)
datos/             Datos congelados, scripts de preparación (agregar_londres.py, preparar_momentum.py), checksums
```
