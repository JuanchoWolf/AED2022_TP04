import os
import pickle

NOMBRE_PROY = "proyectos.csv"
NOMBRE_POPULARES = "populares.dat"


def obtener_proyectos():
    vec_proyectos = []

    if not os.path.exists(NOMBRE_PROY):
        print("El archivo no existe")
        return vec_proyectos # Devuelve un vector vacio

    arch = open(NOMBRE_PROY, mode="rt", encoding="utf8")
    linea = None
    primera_linea = True # Para saltar la primera linea del archivo

    while linea is None or linea != "":
        linea = arch.readline()
        if linea != "" and not primera_linea:
            vec_proyectos.append(linea.strip().split("|"))
          
        primera_linea = False

    return vec_proyectos


def guardar_populares(mat_populares):
    pass