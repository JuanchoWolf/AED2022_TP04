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
        return f"{self.nombre_usuario}|{self.repositorio}|{self.fecha_actualizacion}|{self.lenguaje}|{self.likes}|{self.tags}|{self.url}"

    def __str__(self):
      return "{:<16} | {:<20} | {:<20} | {:<11} | {:<10.2f}k | {:<15} | {:<20}".format(self.nombre_usuario, self.repositorio, self.fecha_actualizacion, self.lenguaje, self.likes, self.tags, self.url)


def cabezera_proyectos():
    return "{:^16} | {:^20} | {:^20} | {:^11} | {:^10} | {:^15} | {:^20}".format("Nombre usuario", "Repositorio", "Fecha actualizacion", "Lenguaje", "Likes", "Tags", "URL") + "\n" + "-" * 140


def convertir_a_proyecto(cadena):
    campos = cadena.split("|")
    return Proyecto(
        campos[0],
        campos[1],
        campos[3],
        campos[4],
        float(campos[5].replace("k", "")),
        campos[6],
        campos[7]
    )


if __name__ == "__main__":
    popularidad = Popularidad(1, 100, 10)
    print(cabera_popularidad())
    print(popularidad)

    proyecto = Proyecto("usuario", "repositorio", "fecha", "lenguaje", 100, "tags", "url")
    print(cabezera_proyectos())
    print(proyecto)
