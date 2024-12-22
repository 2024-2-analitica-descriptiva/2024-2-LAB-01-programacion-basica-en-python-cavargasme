"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
with open("./files/input/data.csv") as file:
    datos = file.readlines()

datos = [line.replace('\t', '|').replace('\n','') for line in datos]
datos = [line.split('|') for line in datos]

from datetime import datetime
from collections import Counter
import itertools

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    datos_suma = []

    for i, j in itertools.groupby(sorted(datos), lambda x : x[0]):
        valores_list = [x[1] for x in j]
        datos_suma.append((i, int(max(valores_list)), int(min(valores_list))))

    return datos_suma