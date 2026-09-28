# Laboratorios computacionales — Cálculo Diferencial · Cálculo Integral · Introducción a las Ciencias de la Computación

Universidad Nacional de Colombia, Sede Manizales · 2026-II

Los tres cursos comparten la misma infraestructura de laboratorio: cuadernos en **Google Colab**, datos congelados en este repositorio, una cuenta de **Kaggle** para ir a la fuente, y una IA que trabaja de tutora, no de autora. Nada que instalar: todo corre en el navegador.

## Empezar aquí

1. Lee la **[Guía Sesión 0](sesion0/Guia_Sesion_0_Antes_del_primer_laboratorio.pdf)**: cuentas, descargas, glosario y la prueba de humo.
2. Abre el cuaderno de tu curso en Colab (enlaces de abajo), guarda tu copia en Drive y trabaja sobre ella.

| Curso | Guía | Cuaderno sesión 1 | Cuaderno sesión 2 |
|---|---|---|---|
| Cálculo Diferencial | [Guía L1](diferencial/Guia_L1_La_factura_de_la_ciudad.pdf) | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/diferencial/L1_sesion1.ipynb) | (próximamente) |
| Cálculo Integral | [Guía L1](integral/Guia_L1_La_factura_de_la_ciudad.pdf) · [gráfica P1](integral/prediccion_P1_enero2013.pdf) | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/integral/L1_sesion1.ipynb) | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/integral/L1_sesion2.ipynb) |
| Introducción a las CC | [Guía L1](introduccion_cc/Guia_L1_La_factura_de_la_ciudad.pdf) (la misma de Diferencial) | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/introduccion_cc/L1_sesion1.ipynb) | — |

## Datos

Todo en [`datos/`](datos/README.md), con huellas MD5. El crudo de Kaggle (`london_energy.csv`, 96 MB) **no** está aquí a propósito: descargarlo de la fuente es la tarea puente.

## Protocolo de IA

Intento propio antes de consultar · la IA no es la autoridad final · todo uso va a la bitácora individual. Detalles en la Guía Sesión 0.

## Estructura

```
sesion0/           Guía común a los tres cursos (fuente .tex y PDF)
diferencial/       Guía L1 + cuaderno sesión 1
integral/          Guía L1 + gráfica de predicción + cuadernos sesiones 1 y 2
introduccion_cc/   Mismo laboratorio que Diferencial
datos/             Datos congelados, script de agregación, checksums
```
