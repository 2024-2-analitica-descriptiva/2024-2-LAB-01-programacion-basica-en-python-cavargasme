"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
   # Lectura del archivo data.csv
with open("./files/input/data.csv") as file:
    datos = file.readlines()

datos = [line.replace('\t', '|').replace('\n','') for line in datos]
datos = [line.split('|') for line in datos]

"""
Retorne la suma de la segunda columna.

Rta/
214

"""
    
def pregunta_01():
    suma = 0
    for lista in datos:
        suma += int(lista[1])

    return suma