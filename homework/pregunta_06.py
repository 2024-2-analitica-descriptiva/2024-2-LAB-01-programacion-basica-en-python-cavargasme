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

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    nueva_lista_valores = []
    datos_dic = []

    valores = [x[4] for x in datos]
    lista_valores = [x.split(",") for x in valores]

    for x in lista_valores:
        for y in x:
            nueva_lista_valores.append(y.split(":"))

    for i, j in itertools.groupby(sorted(nueva_lista_valores), lambda x : x[0]):
        valores_list = [int(x[1]) for x in j]
        datos_dic.append((i, min(valores_list), max(valores_list)))

    return datos_dic