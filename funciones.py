def validar_vacio(num):
    if num.strip() == "":
        return False
    return True


def validar_numero(num):
    if num.isdigit():
        return True
    return False


def validar_positivo(num):
    return int(num) > 0


def validar_conjunto(inf, sup, num):
    return inf <= int(num) <= sup


def validar(): # Validar que sea un numero entero positivo
    num = input("Ingrese un numero mayor a 0: ")
    while not validar_vacio(num) or not validar_numero(num) or not validar_positivo(num):
        print("Error...")
        num = input("Ingrese un numero mayor a 0: ")

    return int(num)


def validar_entre(inf, sup):
    num = input(f"Ingrese un numero entre {inf} y {sup}: ")
    while not validar_vacio(num) or not validar_numero(num) or not validar_conjunto(inf, sup, num):
        print("Error...")
        num = input(f"Ingrese un numero entre {inf} y {sup}: ")

    return int(num)


def es_anio_bisiesto(anio):
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0


def obtener_dias_por_mes_y_anio(mes, anio):
    if mes in (1, 3, 5, 7, 8, 10, 12):  # meses con 31 dias
        return 31
    elif mes in (4, 6, 9, 11):  # meses con 30 dias
        return 30
    elif es_anio_bisiesto(anio):
        return 29
    else:
        return 28


def rellenar_digitos(d, n):
    cad = str(d)
    while len(cad) < n:
        cad = "0" + cad

    return cad


def generar_matriz(filas, columnas, valor):
  return [[valor] * columnas for i in range(filas)]


def dar_formato_fecha(anio, mes, dia):
    # FORMATO: AAAA-MM-DD
    return f"{rellenar_digitos(anio, 4)}-{rellenar_digitos(mes, 2)}-{rellenar_digitos(dia, 2)}"


def descomponer_fecha(fecha):
    anio = int(fecha[:4])
    mes = int(fecha[5:7])
    dia = int(fecha[8:])

    return anio, mes, dia


def cargar_fecha():
    print("Ingrese año (AAAA)...")
    anio = validar_entre(2000, 2022)
    print("Ingrese mes (MM)...")
    mes = validar_entre(1, 12)
    print("Ingrese dia (DD)...")
    fin_mes = obtener_dias_por_mes_y_anio(mes, anio)
    dia = validar_entre(1, fin_mes)

    return dar_formato_fecha(anio, mes, dia)


def representar_diferencia(box):
    # box = [  [lenguaje, cantidad]  ]
    for i in range(len(box)):
        lengugaje = box[i][0]
        cantidad = box[i][1]
        print( "\n__", lengugaje, "ha sido cargado", cantidad, "veces." )

    return


def ordenar_lista_listas(iterable: list, index: int, upper: bool = True) -> None:
    """
    Ordenar Listas de Listas{\n
        iterable = lista\n
        index = id de el objeto de las sublistas a ordenar\n
        upper = determina si se ordena de forma Ascendente(True - por defecto), o Descentente(False)\n
    }
    """
    long = len(iterable)

    for i in range(0, long-1):
        for j in range(i+1, long):

            if iterable[i][index] < iterable[j][index] and not upper:
                iterable[i], iterable[j] = iterable[j], iterable[i]

            elif iterable[i][index] > iterable[j][index] and upper:
                iterable[i], iterable[j] = iterable[j], iterable[i]


def mostrar_por_tags(proyecto, estrellas, saving, flag):
    repo = proyecto.repositorio
    actualizacion = proyecto.fecha_actualizacion

    print("\nRepositorio: ", repo, "Actualizado por ultima vez: ", actualizacion, "Con: ", estrellas, "estrellas.")

    # guardar archivo
    if saving:
        from manejar_archivos import saving_file_tags

        saving_file_tags(proyecto, estrellas, flag)

    return True
