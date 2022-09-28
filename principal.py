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
        elif len(vec_proyectos) > 0:
            if opc == 2:
                tag = input("\nTag que Desea Buscar:   ") # TODO: Validar que no sea vacio
                flag_mostrar = find_tag(tag, vec_proyectos)
                if not flag_mostrar:
                    print('\nNo hay ningun elemento con ese Tag...\n')
                

            elif opc == 3:
                box = discriminar_lenguajes(vec_proyectos)
                ordenar_lista_listas(box, 1, False)
                representar_diferencia(box)

            elif opc == 4:
                mat_populares = obtener_resumen_popularidad(vec_proyectos)
                mostrar_matriz_popularidad(mat_populares)

                print("\n Ingrese el del que desea ver la suma de popularidad: ")
                mes = validar_entre(1, 12) - 1
                print("\nLa suma de popularidad del mes {} es: {}".format(mes + 1, sum(mat_populares[mes])))
            elif opc == 5:
                pass

            elif opc == 6:
                if len(mat_populares) == 0:
                    print("\nNo se ha generado el resumen de popularidad. Vaya a la opcion 4")
                else:
                    pops = resumen_popularidad_a_registro(mat_populares)
                    guardar_populares(pops)
                    print("\nSe ha guardado el archivo de popularidad")

        elif opc == 7:
            print("\nLeyendo archivo...")
            pops = leer_populares()
            mat = generar_matriz(12, 5, 0)

            for pop in pops:
                mat[pop.mes - 1][pop.estrellas - 1] = pop.cant_proy
            
            mat_populares = mat
            mostrar_matriz_popularidad(mat_populares)
                
        else:
            print("\nNo hay proyectos cargados aún. Por favor, cargue proyectos primero. (Opcion 1) \n")


if __name__ == "__main__":
    principal()