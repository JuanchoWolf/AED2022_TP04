import os
import pickle
from registro import *

NOMBRE_PROY = "proyectos.csv"
NOMBRE_POPULARES = "populares.dat"


def obtener_proyectos(vec_proyectos):
    if not os.path.exists(NOMBRE_PROY):
        print("El archivo no existe")
        return 0, 0# Devuelve un vector vacio

    arch = open(NOMBRE_PROY, mode="rt", encoding="utf8")
    linea = None
    primera_linea = True # Para saltar la primera linea del archivo

    procesados = 0
    descartados = 0

    while linea is None or linea != "":
        linea = arch.readline()
        
        if linea != "" and not primera_linea:

            procesar = comprobar_linea(linea, vec_proyectos)

            if procesar:
                procesados += 1

                proy = convertir_a_proyecto(linea)
                asignar_posicion_proyecto(proy, vec_proyectos)

            else:
                descartados += 1

        primera_linea = False

    arch.close()
    print(vec_proyectos)
    return procesados, descartados


def guardar_populares(mat_populares):
    pass


if __name__ == "__main__":
    v = obtener_proyectos()
    print(cabezera_proyectos())
    for p in v:
        print(p)