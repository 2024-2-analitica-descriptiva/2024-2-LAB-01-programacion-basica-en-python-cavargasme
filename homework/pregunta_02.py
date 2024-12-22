"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from collections import Counter

with open("./files/input/data.csv") as file:
    datos = file.readlines()

datos = [line.replace('\t', '|').replace('\n','') for line in datos]
datos = [line.split('|') for line in datos]


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    col1 = []
    [col1.append(item[0]) for item in datos]
    tuple_list = sorted(list(Counter(col1).items()))

    return tuple_list