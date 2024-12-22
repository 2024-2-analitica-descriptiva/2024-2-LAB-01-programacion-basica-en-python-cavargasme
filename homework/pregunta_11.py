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

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    from operator import itemgetter
    col1 = [itemgetter(1)(i) for i in datos]
    col3 = [i[3].split(",") for i in datos]
    new_ = zip(col1,col3)

    new_1 = []
    new_group = []

    for x in list(new_):
        for y in x[1]:
            new_1.append((x[0],y))


    for i, j in itertools.groupby(sorted(new_1, key = lambda x : x[1]), lambda x : x[1]):
        new_group.append((i, sum([int(y[0]) for y in j])))

    return dict(new_group)