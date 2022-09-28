# from funciones import generar_matriz, mostrar_por_tags, descomponer_fecha


class Popularidad:
    def __init__(self, mes, estrellas, cant_proy):
        self.mes = mes
        self.estrellas = estrellas
        self.cant_proy = cant_proy

    def __str__(self):
        return "{:^6} | {:>10.2f}k | {:>10}".format(self.mes, self.estrellas, self.cant_proy)


def cabera_popularidad():
    return "{:^6} | {:>11} | {:>10}".format("Mes", "Estrellas", "Proyectos") + "\n" + "-" * 34


class Proyecto:
    def __init__(self, nombre_usuario, repositorio, fecha_actualizacion, lenguaje, likes, tags, url):
        self.nombre_usuario = nombre_usuario
        self.repositorio = repositorio
        self.fecha_actualizacion = fecha_actualizacion
        self.lenguaje = lenguaje
        self.likes = likes
        self.tags = tags
        self.url = url

    def formato_archivo(self):
        return f"{self.nombre_usuario}|{self.repositorio}|{self.fecha_actualizacion}|{self.lenguaje}|{self.likes}|{','.join(self.tags)}|{self.url}"

    def __str__(self):
        return "{:^16} | {:^20} | {:^12} | {:^11} | {:^5.2f}k | {:^60} | {:^20}".format(self.nombre_usuario, self.repositorio, self.fecha_actualizacion, self.lenguaje, self.likes, ", ".join(self.tags), self.url)


def cabezera_proyectos():
    return "{:^16} | {:^20} | {:^12} | {:^11} | {:^7} | {:^60} | {:^20}".format(
        "Nombre usuario",
        "Repositorio",
        "Fecha Act.",
        "Lenguaje",
        "Likes",
        "Tags",
        "URL") + "\n" + "-" * 180


def convertir_a_proyecto(cadena, sep="|"):
    campos = cadena.split(sep)
    return Proyecto(
        campos[0],
        campos[1],
        campos[3],
        campos[4],
        float(campos[5].replace("k", "")),
        campos[6].split(","),  # Tags
        campos[7]
    )


def busqueda_binaria(proyecto, vec_proyectos):
    n = len(vec_proyectos)
    izq = 0
    der = n - 1
    c = 0

    while izq <= der:
        c = (izq + der) // 2

        if vec_proyectos[c].repositorio.lower() == proyecto.repositorio.lower():
            return -1  # No deben repetirse los repositorios.
        elif vec_proyectos[c].repositorio.lower() > proyecto.repositorio.lower():
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        return izq

    return c


def insetar_proy_ordenado(proyecto, vec_proyectos):
    # Buscar la posición donde se debe insertar el proyecto mediante busqueda binaria
    pos = busqueda_binaria(proyecto, vec_proyectos)
    if pos != -1:
        # Inserta un proyecto en el vector de proyectos
        vec_proyectos[pos:pos] = [proyecto]
        return True

    return False  # Repetido


def comprobar_linea(linea, vec_proyectos):
    campos = linea.split("|")

    # lenguaje en blanco
    if campos[4] == "":
        return False

    return True


def discriminar_lenguajes(vec_proyectos):
    # [  [lenguaje, cantidad]  ]
    lenguajes_cantidad = []

    for i in range(len(vec_proyectos)):
        linea = vec_proyectos[i].lenguaje
        exist = False

        for j in range(len(lenguajes_cantidad)):
            # si se encuentra en la lista lo suma
            if linea == lenguajes_cantidad[j][0]:
                exist = True
                lenguajes_cantidad[j][1] += 1

        # si no lo encuentra lo añade
        if not exist:
            box = [linea, 1]
            lenguajes_cantidad.append(box)

    return lenguajes_cantidad


def buscar_por_tag(tag, vec_proyectos):
    coincidencias = []
    for i in range(len(vec_proyectos)):
        if tag in vec_proyectos[i].tags:
            coincidencias.append(vec_proyectos[i])

    return coincidencias
