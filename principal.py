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


def principal():
    vec_proyectos = []
    mat_populares = []

    opc = 0

    while opc != 8:
        opc = menu()
        
        if opc == 1:
            procesados, descartados = obtener_proyectos(vec_proyectos)
            print('\n\tTotal de Proyectos Cargados:', procesados)
            print('\tTotal de Proyectos Descartados:', descartados)

        elif opc == 2:
            tag = input("\nTag que Desea Buscar:   ")
            flag_mostrar = find_tag(tag, vec_proyectos)
            if not flag_mostrar:
                print('\nNo hay ningun elemento con ese Tag...\n')
            

        elif opc == 3:
            box = discriminar_lenguajes(vec_proyectos)
            box = ordenar_lista_listas(box, True, 1)
            representar_diferencia(box)

        elif opc == 4:
            pass

        elif opc == 5:
            pass

        elif opc == 6:
            pass

        elif opc == 7:
            pass

        else:(exit("Done!"))
      


if __name__ == "__main__":
  principal()