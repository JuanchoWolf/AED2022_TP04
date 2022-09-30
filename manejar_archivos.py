import os
import pickle
from registro import *

NOMBRE_PROY = "proyectos.csv"
NOMBRE_POPULARES = "populares.dat"
NOMBRE_TAGS = "proyectos_por_tags.txt"


def obtener_proyectos(vec_proyectos):
    if not os.path.exists(NOMBRE_PROY):
        print("El archivo no existe")
        return 0, 0  # Devuelve un vector vacio

    arch = open(NOMBRE_PROY, mode="rt", encoding="utf8")
    linea = None
    primera_linea = True  # Para saltar la primera linea del archivo

    descartados = 0

    while linea is None or linea != "":
        linea = arch.readline()
        
        if linea != "" and not primera_linea:
            proy = convertir_a_proyecto(linea)
            if not (comprobar_linea(linea) and insetar_proy_ordenado(proy, vec_proyectos)):
                descartados += 1

        primera_linea = False

    arch.close()
    return len(vec_proyectos), descartados


def guardar_populares(vec_proyectos):
    arch = open(NOMBRE_POPULARES, mode="wb")

    for pop in vec_proyectos:
        pickle.dump(pop, arch)

    arch.close()


def leer_populares():
    if not os.path.exists(NOMBRE_POPULARES):
        print("El archivo no existe")
        return []

    arch = open(NOMBRE_POPULARES, mode="rb")
    vec_pops = []
    t = os.path.getsize(NOMBRE_POPULARES)

    while arch.tell() < t:
        pop = pickle.load(arch)
        vec_pops.append(pop)

    arch.close()
    return vec_pops


def saving_file_tags(vec_proyectos):
    archivo = open(NOMBRE_TAGS, mode="wt", encoding="utf8")

    archivo.write("nombre_usuario|repositorio|fecha_actualizacion|lenguaje|likes|estrellas|tags|url\n")

    for i in range(len(vec_proyectos)):
        archivo.write(vec_proyectos[i].formato_archivo())

    archivo.close()
