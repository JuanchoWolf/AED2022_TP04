from funciones import *

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
    
    op = 0

    while opc != 8:
      opc = menu()
      pass


if __name__ == "__main__":
  principal()