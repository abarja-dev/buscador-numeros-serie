"""
Script que busca números de serie en archivos .txt dentro de un directorio,recibe la ruta por argumento o por input,
e imprime y guarda resultados
"""


import os
import sys
import datetime
import time
import re
import math
import csv

def obtener_ruta():
    """
    Devuelve la ruta del directorio a analizar. La toma de sys.argv si fue pasada como argumento, si no, la pide
    por consola
    """
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return input("Introduce la ruta del directorio a analizar: ")

def exploracion_archivos(ruta):
    """
    Explora todos los archivos .txt dentro del directorio dado
    """
    lista_archivos = []
    for carpeta, subcarpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo.endswith(".txt"):
                lista_archivos.append(os.path.join(carpeta, archivo))
    return lista_archivos

def buscar_patron(lista_archivos, patron):
    """
    Busca el patrón proporcionado en los archivos encontrados
    y devuelve una lista de tuplas (nombre_archivo, coincidencia)
    """
    resultados = []
    for archivo in lista_archivos:
        with open(archivo, "r", encoding='utf-8') as f:
            contenido = f.read()
            coincidencias = re.findall(patron, contenido)
            for coincidencia in coincidencias:
                resultados.append((os.path.basename(archivo), coincidencia))
    return resultados

def imprimir_resultados(resultados, duracion):
    """
    Imprime en pantalla una tabal con los resultados encontrados
    """
    fecha = datetime.date.today().strftime("%d/%m/%Y")
    print("-"*50)
    print(f'fecha de busqueda: {fecha}')
    print('\nARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for archivo, numero in resultados:
        print(f'{archivo:<24}{numero}')
    print(f'\nNúmeros encontrados: {len(resultados)}')
    print(f'Duración de la búsqueda: {duracion} segundos')
    print('-' * 50)

def guardar_csv(resultados):
    """
    Guarda los resultados en un archivo CSV
    """
    with open('resultados_busqueda.csv', 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(['Archivo', 'Número de serie'])
        escritor.writerows(resultados)
    print("Resultados guardados en 'resultados_busqueda.csv'.")

def main():
    """
    Función principal del programa
    """
    ruta = obtener_ruta()

    if not os.path.isdir(ruta):
        print('La ruta proporcionada no es válida')
        return

    patron = r'N\D{3}-\d{5}'

    inicio = time.time()
    archivos = exploracion_archivos(ruta)
    resultados= buscar_patron(archivos, patron)
    duracion = math.ceil(time.time() - inicio)

    if resultados:
        imprimir_resultados(resultados, duracion)
        guardar_csv(resultados)
    else:
        print('No se encontraron coincidencias con el patrón')

if __name__ == '__main__':
    main()


