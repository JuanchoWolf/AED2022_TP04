
NOMBRE_ARCHIVO = "proyectos.csv"

def obtener_contenido():
    contenido = ""

    # TODO: AGREGAR VERIFICACIÓN DE EXISTENCIA DE ARCHIVO

    arch = open(NOMBRE_ARCHIVO, mode="rt", encoding="utf8")
    contenido = arch.readlines()
    arch.close()

    return contenido