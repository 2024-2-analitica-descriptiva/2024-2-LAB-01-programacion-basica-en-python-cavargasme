"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
with open("/home/camila/Escritorio/A. Descriptiva/Laboratorios/2024-2-LAB-01-programacion-basica-en-python-cavargasme/files/input/data.csv","r") as file:
    datos = file.readlines()

datos = [line.replace('\t', '|').replace('\n','') for line in datos]
datos = [line.split('|') for line in datos]

from datetime import datetime
from collections import Counter
import itertools

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    from operator import itemgetter

    columnas = [itemgetter(0,3,4)(i) for i in datos]
    conteo = []

    for x in columnas:

        col4 = len(x[1].split(","))
        col5 = len(x[2].split(","))
        conteo.append((x[0], col4, col5))
    return conteo