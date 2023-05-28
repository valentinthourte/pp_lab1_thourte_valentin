from Validaciones.validaciones_texto import *
from Funciones.funciones_mostrar import imprimir

def menu_principal(texto_input):
    cantidad_opciones = imprimir_menu_parcial()
    opcion = input(texto_input)
    return validar_opcion(opcion, cantidad_opciones)

def imprimir_menu_parcial():
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
    "0. Salir"
    ]
    imprimir_menu(lista_opciones)
    return len(lista_opciones)

def pedir_opcion_hasta__que_sea_valida(texto_input = "Ingrese una opción para continuar: "):
    opcion = menu_principal(texto_input)
    while opcion == -1:
        opcion = menu_principal(texto_input)
    return int(opcion)


def imprimir_menu(lista):
    for opcion in lista:
        imprimir([opcion])