from funciones import *
from manejar_archivos import *

# Consignas
# https://uv.frc.utn.edu.ar/mod/assign/view.php?id=192765 


# Mostrar menu y solicitar opcion
def menu():
    cad_menu = f"""\nMenu de opciones
        {"-" * 50}
        1. Cargar proyectos
        2. Filtrar por tag
        3. Resumen por lenguaje
        4. Resumen por popularidad
        5. Buscar proyecto actualizado
        6. Guardar populares en archivo
        7. Mostrar archivo
        8. Salir
        {"-" * 50}
        Ingrese opcion...
        """
    print(cad_menu)
    op = validar_entre(1, 8)

    return op


# Filtrar por TAG y permitir guardar
def opcion2(vec_proyectos):
    tag = solicitar_cadena("Tag que Desea Buscar:   ")
    coincidencias = buscar_por_tag(tag, vec_proyectos)

    if len(coincidencias) > 0:
        print("\nProyectos con el tag {}:".format(tag))
        print("{:30} | {:<12} | {:<10}".format("Nombre", "Fecha", "Estrellas"))
        print("-" * 60)
        for c in coincidencias:
            print("{:30} | {:<12} | {:<10}".format(c.repositorio, c.fecha_actualizacion, obtener_rango(c.likes)))

        print("\nDesear guardar los resultados en un archivo? (Si:1 - No:2)")
        guardar = validar_entre(1, 2)

        if guardar == 1:
            saving_file_tags(coincidencias)
            print("\nSe ha guardado el archivo de proyectos")
    else:
        print('\nNo hay ningun elemento con ese Tag...\n')


# Mostrar lista por lenguaje
def opcion3(vec_proyectos):
    box = discriminar_lenguajes(vec_proyectos)
    ordenar_lista_listas(box, 1, False)
    representar_diferencia(box)


def opcion4(mat_populares, vec_proyectos):
    mat_populares = obtener_resumen_popularidad(vec_proyectos)
    mostrar_matriz_popularidad(mat_populares)

    print("\n Ingrese el del que desea ver la suma de popularidad: ")
    mes = validar_entre(1, 12) - 1
    print("\nLa suma de popularidad del mes {} es: {}".format(mes + 1, sum(mat_populares[mes])))
    return mat_populares


# Buscar por repositorio y actualizar URL y fecha
def opcion_5(vec_proy, repo):
    c = 0
    n = len(vec_proy)
    izq = 0
    der = n - 1

    while izq <= der:
        c = (izq + der) // 2
        if vec_proy[c].repositorio.lower() == repo.lower():
            print("\nSe ha encontrado el proyecto {} en la posicion {}".format(repo, c+1))
            print("Ingrese la nueva URL del proyecto: ")
            vec_proy[c].url = solicitar_cadena("URL: ")
            vec_proy[c].fecha_actualizacion = fecha_hoy()
            print("Se ha actualizado el proyecto")
            return
        elif repo.lower() < vec_proy[c].repositorio.lower():
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        print("\nNo se ha encontrado el proyecto {} en el vector".format(repo))


# Guardar tabla de popularidad en archivo
def opcion6(mat_populares):
    if len(mat_populares) == 0:
        print("\nNo se ha generado el resumen de popularidad. Vaya a la opcion 4")
    else:
        pops = resumen_popularidad_a_registro(mat_populares)
        guardar_populares(pops)
        print("\nSe ha guardado el archivo de popularidad")


# Mostrar archivo guardado
def opcion7():
    print("\nLeyendo archivo...")
    pops = leer_populares()

    if len(pops) == 0:
        print("\nNo se ha guardado el resumen de popularidad. Vaya a la opcion 6")
        return

    mat = generar_matriz(12, 5, 0)

    for pop in pops:
        mat[pop.mes - 1][pop.estrellas - 1] = pop.cant_proy

    mostrar_matriz_popularidad(mat)


def principal():
    vec_proyectos = []
    mat_populares = []

    opc = 0

    while opc != 8:
        opc = menu()
    
        if opc == 8:
            print("Hasta luego!")
            return
        elif opc == 1:
            procesados, descartados = obtener_proyectos(vec_proyectos)
            for i in range(len(vec_proyectos)):
                print(i+1, vec_proyectos[i].repositorio)
            print('\n\tTotal de Proyectos Cargados:', procesados)
            print('\tTotal de Proyectos Descartados:', descartados)
        elif opc == 7:
            opcion7()
        elif len(vec_proyectos) > 0:
            if opc == 2:
                opcion2(vec_proyectos)
            elif opc == 3:
                opcion3(vec_proyectos)
            elif opc == 4:
                mat_populares = opcion4(vec_proyectos)
            elif opc == 5:
                rep = solicitar_cadena("Ingrese nombre del repositorio buscado: ")
                opcion_5(vec_proyectos, rep)
            elif opc == 6:
                opcion6(mat_populares)

        elif len(vec_proyectos) == 0:
            print("\nNo hay proyectos cargados aún. Por favor, cargue proyectos primero. (Opcion 1) \n")
    
        input("\nPulse enter para continuar...")


if __name__ == "__main__":
    principal()
