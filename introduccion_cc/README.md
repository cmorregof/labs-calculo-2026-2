# Introducción a las Ciencias de la Computación — L1 · Primer contacto

**¿Cómo se le escribe a alguien que no sabe nada de nosotros?**

El 16 de noviembre de 1974, el radiotelescopio de Arecibo mandó hacia el cúmulo de estrellas M13 un mensaje de 1 679 bits, sin idioma y sin instrucciones. En la sesión 1 ustedes lo reciben y lo descifran con funciones que programan. En la sesión 2 cada equipo es una especie que cuenta en su propia base, y le escribe a otra especie del salón un mensaje que tiene que sobrevivir a un canal con ruido.

Dos sesiones de 2 horas y una tarea puente · equipos de 3 o 4 · Python en Colab. Lean primero la [guía](Guia_L1_Primer_contacto.pdf).

| Cuaderno | Qué se hace | |
|---|---|---|
| `L1_sesion1.ipynb` | Recibir: descifrar Arecibo | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/introduccion_cc/L1_sesion1.ipynb) |
| `L1_tarea_puente.ipynb` | Reproducir el dato, cambiar de base de dos maneras, diseñar la especie | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/introduccion_cc/L1_tarea_puente.ipynb) |
| `L1_sesion2.ipynb` | Responder: escribir, proteger y mandar el mensaje; leer uno ajeno | [Abrir en Colab](https://colab.research.google.com/github/cmorregof/labs-calculo-2026-2/blob/main/introduccion_cc/L1_sesion2.ipynb) |

Al abrir un cuaderno, lo primero es **Archivo → Guardar una copia en Drive**. Si trabajan sobre el original, al cerrar la pestaña se pierde todo. Al final, **Archivo → Guardar una copia en GitHub**, en su repositorio `intro-cc`.

## Cómo están hechos los cuadernos

- Las preguntas de **Momento 1** se contestan en papel, antes de tocar el computador. La foto va al cuaderno.
- Cada función trae su **contrato** (qué recibe, qué devuelve, qué supone) y un espacio `# TU CÓDIGO AQUÍ`.
- Debajo de cada función hay **pruebas** con `assert`. Si una falla, la celda muestra un `AssertionError`: es la máquina diciéndoles dónde mirar.
- Las celdas marcadas **CAJA** ya vienen hechas. Basta con entender su contrato.
- Donde aparece ✍️, se responde en texto.

## Archivos

| Archivo | Qué es |
|---|---|
| `Guia_L1_Primer_contacto.pdf` | La guía del laboratorio |
| `L1_sesion1.ipynb`, `L1_tarea_puente.ipynb`, `L1_sesion2.ipynb` | Los cuadernos |
| `congelar_arecibo.py` | Trae el mensaje de su fuente original, lo valida y lo congela |
| `../datos/arecibo.txt` | El mensaje congelado: una línea de 1 679 caracteres `0`/`1` |
| `bitacora_IA_L1.md` | Plantilla de la bitácora de IA (individual) |
| `factura_sesion1/` | La sesión 1 de *La factura de la ciudad* (compartida con Diferencial), archivada aquí |

## Cifras de control

Si su copia del mensaje es correcta (tarea puente, parte A), debe dar exactamente:

| | |
|---|---|
| Caracteres | 1 679 |
| Unos | 397 |
| SHA-256 | `24babf56f872fc2c38c940b4a438811be454f04a041fe56b3c239662f261dd66` |

Si algo no cuadra, no está "casi bien": hay una diferencia, y encontrarla es la tarea.

## Entregables (cierre de la semana de la sesión 2)

1. Los tres cuadernos del equipo, ejecutados de arriba a abajo sin errores, con las fotos de las predicciones y los tres momentos completos, en el repositorio `intro-cc` de cada integrante.
2. `mensaje.txt` con los bits que mandó su especie, en el mismo repositorio.
3. La bitácora de IA individual (una página).
4. En el cuaderno de la tarea puente: la verificación reproducida, el cambio de base de dos maneras con la tabla de la pila, y el contrato de lectura escrito antes de la sesión 2.

## Protocolo de IA

Intento propio antes de consultar · la IA no es la autoridad final · todo uso va a la bitácora (el prompt exacto, qué salió, qué se aceptó, corrigió o rechazó, y cómo se comprobó). Prohibido pedirle las funciones de los cuadernos, el contrato de lectura, el diseño del mensaje o los momentos 3.
