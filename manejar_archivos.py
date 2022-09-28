import os
import pickle
from registro import *

NOMBRE_PROY = "proyectos.csv"
NOMBRE_POPULARES = "populares.dat"


def obtener_proyectos(vec_proyectos):
    if not os.path.exists(NOMBRE_PROY):
        print("El archivo no existe")
        return 0, 0 # Devuelve un vector vacio

    arch = open(NOMBRE_PROY, mode="rt", encoding="utf8")
    linea = None
    primera_linea = True # Para saltar la primera linea del archivo

    descartados = 0

    while linea is None or linea != "":
        linea = arch.readline()
        
        if linea != "" and not primera_linea:
            proy = convertir_a_proyecto(linea)
            if not (comprobar_linea(linea, vec_proyectos) and insetar_proy_ordenado(proy, vec_proyectos)):
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


def saving_file_tags(proyecto, estrellas, flag):
    archivo = open('proyectos_por_tags.txt', mode="at", encoding="utf8") # mode= 'anexar texto'

    user = proyecto.nombre_usuario
    repo = proyecto.repositorio
    actualizacion = proyecto.fecha_actualizacion
    lenguaje = proyecto.lenguaje
    tags = proyecto.tags
    url = proyecto.url
    likes = proyecto.likes

    inicial = "nombre_usuario | repositorio | fecha_actualizacion | lenguaje | likes | estrellas | tags | url\n"
    cadena = f"{user}|{repo}|{actualizacion}|{lenguaje}|{likes}|{estrellas}|{tags}|{url}"

    if flag:
        archivo.write(inicial)
        archivo.write(cadena)

    if not flag:
        archivo.write(cadena)

    archivo.close()


if __name__ == "__main__":
    v = obtener_proyectos()
    print(cabezera_proyectos())
    for p in v:
        print(p)
