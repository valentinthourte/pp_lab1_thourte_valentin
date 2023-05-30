from Validaciones.validaciones import *
from Funciones.funciones_mostrar import imprimir

def menu_principal(texto_input):
    """
    Muestra el menú principal y solicita al usuario que ingrese una opción. 

    Recibe:
    - texto_input: Texto que se muestra al solicitar la opción al usuario.

    Devuelve:
    - Opción ingresada por el usuario como entero. Si la opcion no es valida, se vuelve a solicitar hasta que lo sea.
    """
    cantidad_opciones = imprimir_menu_parcial()
    opcion = input(texto_input)
    return validar_opcion(opcion, cantidad_opciones)

def imprimir_menu_parcial():
    """
    Imprime el menú principal y devuelve la cantidad de opciones disponibles.

    No recibe ningún parámetro.

    Devuelve:
    - Cantidad de opciones disponibles en el menú como entero.
    """
    lista_opciones = [
    "1. Mostrar la lista de todos los jugadores del Dream Team.",
    "2. Seleccionar un jugador por su índice y mostrar sus estadísticas completas.",
    "3. Guardar las estadísticas de un jugador seleccionado en un archivo CSV.",
    "4. Buscar un jugador por su nombre y mostrar sus logros.",
    "5. Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre.",
    "6. Verificar si un jugador es miembro del Salón de la Fama del Baloncesto.",
    "7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.",
    "8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.",
    "9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.",
    "10. Mostrar jugadores con promedio de puntos por partido superior a un valor dado.",
    "11. Mostrar jugadores con promedio de rebotes por partido superior a un valor dado.",
    "12. Mostrar jugadores con promedio de asistencias por partido superior a un valor dado.",
    "13. Calcular y mostrar el jugador con la mayor cantidad de robos totales.",
    "14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.",
    "15. Mostrar jugadores con porcentaje de tiros libres superior a un valor dado.",
    "16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.",
    "17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.",
    "18. Mostrar jugadores con porcentaje de tiros triples superior a un valor dado.",
    "19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.",
    "20. Mostrar jugadores ordenados por posición en la cancha con porcentaje de tiros de campo superior a un valor dado.",
    "21. Guardar rankings de jugadores a csv.",
    "22. Mostrar la cantidad de jugadores que hay por cada posición.",
    "23. Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente",
    "24. Determinar qué jugador tiene las mejores estadísticas en cada valor.",
    "25. Mostrar el jugador con mejores estadísticas.",
    "0. Salir"
    ]
    imprimir_menu(lista_opciones)
    return len(lista_opciones) - 1

def pedir_opcion_hasta__que_sea_valida(texto_input="Ingrese una opción para continuar: "):
    """
    Solicita al usuario que ingrese una opción válida del menú principal hasta que lo haga.

    Recibe:
    - texto_input: Texto que se muestra al solicitar la opción al usuario.

    Devuelve:
    - Opción válida ingresada por el usuario como entero.
    """
    opcion = menu_principal(texto_input)
    while opcion == -1:
        texto_error = "Ingrese un valor válido, numérico positivo: "
        opcion = menu_principal(texto_error)
    return int(opcion)

def imprimir_menu(lista):
    """
    Imprime el menú con las opciones disponibles.

    Recibe:
    - lista: Lista de las opciones del menú a imprimir.

    No devuelve ningún valor.
    """
    for opcion in lista:
        imprimir([opcion])

def pedir_indice(cantidad_jugadores):
    """
        Solicita un índice para un jugador y lo devuelve una vez validado

        Parámetros: 
        cantidad_jugadores(int): La cantidad de jugadores, para hacer la validación

        Devuelve: El índice resultante (int)
    """
    indice = input("Ingrese un índice.")
    return validar_indice(indice, cantidad_jugadores)

def pedir_nombre(nombre_completo):
    """
    Solicita un nombre para un jugador y lo devuelve una vez validado

    Parámetros: 
    nombre_completo(bool): Utilizado para la validación, determina si debería buscarse por nombre completo o por coincidencia de comienzo

    Devuelve: El nombre resultante (str)
    """
    nombre = input("Ingrese un nombre: ")
    return validar_nombre(nombre, nombre_completo)

def pedir_valor_para_promedio():
    """
        Solicita un valor para las comparaciones de promedio y lo devuelve una vez validado

        Parámetros: No tiene

        Devuelve: El valor resultante(int). El mismo será un numero positivo
    """
    valor = input("Ingrese un valor para el promedio: ")
    return validar_valor(valor)