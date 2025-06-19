# Buscador de número de serie en archivos de texto

Aplicación sencilla en Python que busca números de serie con un patrón específico dentro de archivos `.txt` ubicados en
un directorio y sus subdirectorios. Imprime una tabla con los resultados encontrados y los guarda en un archivo CSV.

---

## Descripción

Este script explora una carpeta dada buscando archivos `.txt` y dentro de ellos, detecta números de serie que sigan el
patrón `NXXX-12345` (donde `X` es una letra y los números un grupo de 5 dígitos).
La búsqueda se realiza sobre una estructura de carpetas con subcarpetas, por ejemplo, para textos clásicos en latín
divididos por obras y capítulos.
El resultado se muestra en consola y se guarda en un archivo CSV para su posterior análisis.

---

## Características

- Exploración recursiva de directorios y subdirectorios.
- Búsqueda de patrones con expresiones regulares.
- Reporte de resultados en consola en formato tabla.
- Exportación de resultados a archivo CSV.
- Soporte para recibir la ruta del directorio por argumento o por input.
- Estructura de archivos de prueba organizada por carpetas (`ejemplos/Aeneida`, etc.).

---

## Tecnologías y Requisitos

- Python 3.6 o superior (recomendado Python 3.8+).
- No requiere librerías externas (usa solo librerías estándar: `os`, `re`, `csv`, etc.).

---


## Instalación y Ejecución

1. Clona este repositorio y navega a la carpeta raíz del proyecto:
    ```bash
    git clone https://github.com/abarja-dev/buscador-numeros-serie.git
   ```
2. Ejecuta el script, pasando como argumento la ruta a la carpeta con archivos `.txt`
   (por ejemplo la carpeta ejemplos incluida):
    ```bash
    python buscador.py ejemplos
   ```
   Si no pasas argumento, el programa solicitará la ruta mediante input.

---

## Archivos de ejemplo:
   Los textos de prueba incluidos pertenecen a obras clásicas en latín:

   - Aeneida de Virgilio

   - De Bello Gallico de Julio César

   - Metamorphoseis (Las Metamorfosis) de Ovidio

   Se han insertado algunos números de serie artificiales en los textos para que el script los pueda detectar.
   Esta estructura permite probar la funcionalidad de forma realista y ordenada.
   
---

## Uso
- Al ejecutar el script, se muestra una tabla con los archivos donde se encontraron números de serie
   y los números detectados.
- También se genera un archivo `resultados_busqueda.csv` con el resumen de la búsqueda.
- El tiempo que tardó la búsqueda y la fecha se muestran en consola.

---

## Autor
Alberto Barja Montes