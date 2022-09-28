from funciones import *
from manejar_archivos import *

# Consignas
# https://uv.frc.utn.edu.ar/mod/assign/view.php?id=192765 


# Mostrar menu y solicitar opcion
def menu():
    menu = f"""\nMenu de opciones
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
    print(menu)
    op = validar_entre(1, 8)

    return op


def mostrar_matriz_popularidad(mat):
    print("Resumen de Popularidad")
    print("{:3}|{:10}|{:10}|{:10}|{:10}|{:10}".format("Mes", "0-10", "10-20", "20-30", "30-40", "40-♾️"))
    print("-" * 60)

    for i in range(len(mat)):
        print("{:3}|".format(i + 1), end="")
        for j in range(len(mat[i])):
            print("{:10}|".format(mat[i][j]), end="")
        print()


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


def opcion4(mat_populares, vec_proyectos):
    mat_populares = obtener_resumen_popularidad(vec_proyectos)
    mostrar_matriz_popularidad(mat_populares)

    print("\n Ingrese el del que desea ver la suma de popularidad: ")
    mes = validar_entre(1, 12) - 1
    print("\nLa suma de popularidad del mes {} es: {}".format(mes + 1, sum(mat_populares[mes])))


def opcion_5(vec_proy, repo):
    n = len(vec_proy)
    for i in range(n):
        if vec_proy[i].repositorio == repo:
            print(cabezera_proyectos())
            print(vec_proy[i])
            print()
            nueva_url = validar_vacio(input("Ingrese nueva URL: "))
            while not nueva_url:
                nueva_url = validar_vacio(input("Ingrese nueva URL: "))
            vec_proy[i].url = nueva_url
            vec_proy[i].fecha_actualizacion = str(fecha_hoy())
            print(vec_proy[i])
            return
    print("\nNo se encontro el repositorio...")
    return


def opcion6(mat_populares):
    if len(mat_populares) == 0:
        print("\nNo se ha generado el resumen de popularidad. Vaya a la opcion 4")
    else:
        pops = resumen_popularidad_a_registro(mat_populares)
        guardar_populares(pops)
        print("\nSe ha guardado el archivo de popularidad")


def opcion7(mat_populares):
    print("\nLeyendo archivo...")
    pops = leer_populares()
    mat = generar_matriz(12, 5, 0)

    for pop in pops:
        mat[pop.mes - 1][pop.estrellas - 1] = pop.cant_proy
            
    mat_populares = mat
    mostrar_matriz_popularidad(mat_populares)


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

            print('\n\tTotal de Proyectos Cargados:', procesados)
            print('\tTotal de Proyectos Descartados:', descartados)
            input("\nPulse enter para continuar...")

        elif len(vec_proyectos) > 0:
            if opc == 2:
                opcion2(vec_proyectos)
                input("\nPulse enter para continuar...")

            elif opc == 3:
                box = discriminar_lenguajes(vec_proyectos)
                ordenar_lista_listas(box, 1, False)
                representar_diferencia(box)
                input("\nPulse enter para continuar...")

            elif opc == 4:
                opcion4(mat_populares, vec_proyectos)
                input("\nPulse enter para continuar...")

            elif opc == 5:
                rep = validar_vacio(input("\nIngrese nombre del repositorio buscado: "))
                while not rep:
                    rep = validar_vacio(input("\nIngrese nombre del repositorio buscado: "))
                opcion_5(vec_proyectos, rep)
                input("\nPulse enter para continuar...")

            elif opc == 6:
                opcion6(mat_populares)
                input("\nPulse enter para continuar...")

        elif opc == 7:
            opcion7(mat_populares)
            input("\nPulse enter para continuar...")
        else:
            print("\nNo hay proyectos cargados aún. Por favor, cargue proyectos primero. (Opcion 1) \n")
            input("\nPulse enter para continuar...")


if __name__ == "__main__":
    principal()
