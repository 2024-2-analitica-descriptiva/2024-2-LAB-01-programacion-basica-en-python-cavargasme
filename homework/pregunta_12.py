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

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    from operator import itemgetter
    col0 = [itemgetter(0)(i) for i in datos]
    col4 = [i[4].split(",") for i in datos]


    valores = []
    a = 0

    for x in col4:
        for y in x:
            a += int(y[y.index(":")+1:])


        valores.append(a)
        a = 0


    new_ = list(zip(col0, valores))
    new_group = []

    for i, j in itertools.groupby(sorted(new_, key = lambda x : x[0]), lambda x : x[0]):
        new_group.append((i, sum(y[1] for y in j)))

    return dict(new_group)