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
    return procesados, descartados


def guardar_populares(mat_populares):
    pass


def saving_file_tags(vec_proyectos, i, estrellas, flag):
    archivo = open('proyectos_por_tags.txt', mode="at", encoding="utf8") # mode= 'anexar texto'

    user = vec_proyectos[i].nombre_usuario
    repo = vec_proyectos[i].repositorio
    actualizacion = vec_proyectos[i].fecha_actualizacion
    lenguaje = vec_proyectos[i].lenguaje
    tags = vec_proyectos[i].tags
    url = vec_proyectos[i].url
    likes = vec_proyectos[i].likes

    inicial = "nombre_usuario | repositorio | fecha_actualizacion | lenguaje | likes | estrellas | tags | url\n"
    cadena = f"{user}|{repo}|{actualizacion}|{lenguaje}|{likes}|{estrellas}|{tags}|{url}"

    if flag:
        #print('PASA BIEN')
        archivo.write(inicial)
        #archivo.seek(0, 2)
        archivo.write(cadena)

    if not flag:
        #archivo.seek(0, 2) # desde el final
        archivo.write(cadena)

    archivo.close()


if __name__ == "__main__":
    v = obtener_proyectos()
    print(cabezera_proyectos())
    for p in v:
        print(p)