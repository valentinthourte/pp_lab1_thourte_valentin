from Funciones.funciones_calcular import *
from Funciones.funciones_encontrar import *
from Pantalla.imprimir import imprimir
from Archivos.archivos import *

def imprimir_logros(jugador):
    """
    Imprime los logros de un jugador.

    Recibe:
    - jugador: diccionario con la información del jugador.

    Devuelve:
    No devuelve nada.
    """
    logros = jugador[constantes.LOGROS]
    imprimir([jugador[constantes.NOMBRE]])
    imprimir(logros)


def mostrar_logros_por_nombre(lista_jugadores, nombre):
    """
    Muestra los logros de los jugadores que coinciden con un nombre dado.

    Recibe:
    - lista_jugadores: lista de diccionarios con la información de los jugadores.
    - nombre: nombre a buscar.

    Devuelve:
    No devuelve nada.
    """
    jugadores = encontrar_jugadores_por_clave(lista_jugadores, constantes.NOMBRE, nombre)
    if len(jugadores) == 0:
        print("No existe jugador con ese nombre.")
        return
    else:
        for jugador in jugadores:
            imprimir_logros(jugador)


def imprimir_jugadores_y_estadisticas(lista_jugadores, estadisticas, es_porcentaje=False, agregar_posicion=False):
    """
    Imprime los jugadores y sus estadísticas.

    Recibe:
    - lista_jugadores: lista de diccionarios con la información de los jugadores.
    - estadisticas: lista de estadísticas a imprimir.
    - es_porcentaje (opcional): indica si las estadísticas son porcentajes.
    - agregar_posicion (opcional): indica si se debe agregar la posición del jugador.

    Devuelve:
    No devuelve nada.
    """
    lista_imprimir = []
    for jugador in lista_jugadores:
        texto = obtener_nombre_y_estadisticas(jugador, estadisticas)
        if es_porcentaje:
            texto += "%"
        if agregar_posicion:
            texto += f" - {obtener_clave_y_dato(jugador, constantes.POSICION)}"
        lista_imprimir.append(texto)
    imprimir(lista_imprimir)


def mostrar_jugadores_promedian_mas_puntos_por_partido(lista_jugadores, valor):
    """
    Muestra los jugadores que promedian más puntos por partido que un valor dado.

    Recibe:
    - lista_jugadores: lista de diccionarios con la información de los jugadores.
    - valor: valor a comparar.

    Devuelve:
    No devuelve nada.
    """
    jugadores = obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, constantes.PROMEDIO_PUNTOS_POR_PARTIDO)
    if len(jugadores) == 0:
        print("No hay jugadores que superen ese valor de promedio de puntos por partido.")
    else:
        imprimir_jugadores_y_estadisticas(jugadores, [constantes.PROMEDIO_PUNTOS_POR_PARTIDO])


def mostrar_jugadores_promedian_mas_rebotes_por_partido(lista_jugadores, valor):
    """
    Muestra los jugadores que promedian más rebotes por partido que un valor dado.

    Recibe:
    - lista_jugadores: lista de diccionarios con la información de los jugadores.
    - valor: valor a comparar.

    Devuelve:
    No devuelve nada.
    """
    jugadores = obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, constantes.PROMEDIO_REBOTES_POR_PARTIDO)
    if len(jugadores) == 0:
        print("No hay jugadores que superen ese valor de promedio de rebotes por partido.")
    else:
        imprimir_jugadores_y_estadisticas(jugadores, [constantes.PROMEDIO_REBOTES_POR_PARTIDO])


def mostrar_jugadores_promedian_mas_asistencias_por_partido(lista_jugadores, valor):
    """
    Muestra los jugadores que promedian más asistencias por partido que un valor dado.

    Recibe:
    - lista_jugadores: lista de diccionarios con la información de los jugadores.
    - valor: valor a comparar.

    Devuelve:
    No devuelve nada.
    """
    jugadores = obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, constantes.PROMEDIO_ASISTENCIAS_POR_PARTIDO)
    if len(jugadores) == 0:
        print("No hay jugadores que superen ese valor de promedio de asistencias por partido.")
    else:
        imprimir_jugadores_y_estadisticas(jugadores, [constantes.PROMEDIO_ASISTENCIAS_POR_PARTIDO])


def mostrar_jugadores_promedian_mas_porcentaje_tiros_libres(lista_jugadores, valor):
    """
    Muestra los jugadores que promedian un porcentaje de tiros libres mayor a un valor dado.

    Recibe:
    - lista_jugadores: lista de diccionarios con la información de los jugadores.
    - valor: valor a comparar.

    Devuelve:
    No devuelve nada.
    """
    jugadores = obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, constantes.PORCENTAJE_TIROS_LIBRES)
    if len(jugadores) == 0:
        print("No hay jugadores que superen ese porcentaje de tiros libres.")
    else:
        imprimir_jugadores_y_estadisticas(jugadores, [constantes.PORCENTAJE_TIROS_LIBRES], True)


def mostrar_jugadores_promedian_mas_porcentaje_tiros_triples(lista_jugadores, valor):
    """
    Muestra los jugadores que promedian un porcentaje de tiros triples mayor a un valor dado.

    Recibe:
    - lista_jugadores: lista de diccionarios con la información de los jugadores.
    - valor: valor a comparar.

    Devuelve:
    No devuelve nada.
    """
    jugadores = obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, constantes.PORCENTAJE_TIROS_TRIPLES)
    if len(jugadores) == 0:
        print("No hay jugadores que superen ese porcentaje de tiros triples.")
    else:
        imprimir_jugadores_y_estadisticas(jugadores, [constantes.PORCENTAJE_TIROS_TRIPLES], True)


def mostrar_jugadores_promedian_mas_porcentaje_tiros_campo_por_posicion(lista_jugadores, valor):
    """
    Muestra los jugadores que promedian un porcentaje de tiros de campo mayor a un valor dado, ordenados por posición.

    Recibe:
    - lista_jugadores: lista de diccionarios con la información de los jugadores.
    - valor: valor a comparar.

    Devuelve:
    No devuelve nada.
    """
    jugadores = obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, constantes.PORCENTAJE_TIROS_DE_CAMPO)
    if len(jugadores) == 0:
        print("No hay jugadores que superen ese porcentaje de tiros de campo.")
    else:
        jugadores_ordenados = ordenar_por_posicion_cancha(jugadores, constantes.POSICION)
        imprimir_jugadores_y_estadisticas(jugadores_ordenados, [constantes.PORCENTAJE_TIROS_DE_CAMPO], True, True)

def guardar_ranking_jugadores(lista_jugadores, lista_rankings):
    """
    Guarda el ranking de jugadores por estadísticas en un archivo CSV.

    Recibe:
    - lista_jugadores: Lista de diccionarios que representan a los jugadores.
    - lista_rankings: Lista de estadísticas por las cuales se calculará el ranking.

    No devuelve ningún valor.
    """
    diccio_ranking = obtener_jugadores_rankeados_por_estadisticas(lista_jugadores, lista_rankings)
    guardar_rankings_a_csv(diccio_ranking, lista_rankings)

def mostrar_jugador_mas_temporadas_jugadas(lista_jugadores):
    """
    Muestra el jugador que ha jugado más temporadas.

    Recibe:
    - lista_jugadores: Lista de diccionarios que representan a los jugadores.

    No devuelve ningún valor.
    """
    jugador = obtener_jugador_mas_temporadas_jugadas(lista_jugadores)
    imprimir([obtener_nombre_y_estadisticas(jugador, [constantes.TEMPORADAS])])

def mostrar_jugador_mayor_rebotes_totales(lista_jugadores):
    """
    Muestra el jugador con la mayor cantidad de rebotes totales.

    Recibe:
    - lista_jugadores: Lista de diccionarios que representan a los jugadores.

    No devuelve ningún valor.
    """
    jugador = obtener_jugador_mayor_rebotes_totales(lista_jugadores)
    imprimir([obtener_nombre_y_estadisticas(jugador, [constantes.REBOTES_TOTALES])])

def mostrar_jugador_mayor_porcentaje_tiros_campo(lista_jugadores):
    """
    Muestra el jugador con el mayor porcentaje de tiros de campo.

    Recibe:
    - lista_jugadores: Lista de diccionarios que representan a los jugadores.

    No devuelve ningún valor.
    """
    jugador = obtener_jugador_mayor_porcentaje_tiros_campo(lista_jugadores)
    imprimir([f"{obtener_nombre_y_estadisticas(jugador, [constantes.PORCENTAJE_TIROS_DE_CAMPO])}%"])

def mostrar_jugador_mayor_robos_totales(lista_jugadores):
    """
    Muestra el jugador con la mayor cantidad de robos totales.

    Recibe:
    - lista_jugadores: Lista de diccionarios que representan a los jugadores.

    No devuelve ningún valor.
    """
    jugador = obtener_jugador_mayor_robos_totales(lista_jugadores)
    imprimir([obtener_nombre_y_estadisticas(jugador, [constantes.ROBOS_TOTALES])])

def mostrar_jugador_mayor_bloqueos_totales(lista_jugadores):
    """
    Muestra el jugador con la mayor cantidad de bloqueos totales.

    Recibe:
    - lista_jugadores: Lista de diccionarios que representan a los jugadores.

    No devuelve ningún valor.
    """
    jugador = obtener_jugador_mayor_bloqueos_totales(lista_jugadores)
    imprimir([obtener_nombre_y_estadisticas(jugador, [constantes.BLOQUEOS_TOTALES])])

def mostrar_jugador_mayor_asistencias(lista_jugadores):
    """
    Muestra el jugador con la mayor cantidad de asistencias totales.

    Recibe:
    - lista_jugadores: Lista de diccionarios que representan a los jugadores.

    No devuelve ningún valor.
    """
    jugador = obtener_jugador_mayor_asistencias(lista_jugadores)
    imprimir([obtener_nombre_y_estadisticas(jugador, [constantes.ASISTENCIAS_TOTALES])])

def imprimir_promedio_y_estadistica(estadistica, lista_jugadores, ascendente):
    """
    Imprime una estadística de cada jugador y el promedio de la misma entre todos los jugadores, ordenados por nombre.

    Recibe:
    - estadistica: La estadística de la cual se calculará el promedio.
    - lista_jugadores: Lista de diccionarios que representan a los jugadores.
    - ascendente: Booleano que indica si se ordenará de forma ascendente (True) o descendente (False).

    No devuelve ningún valor.
    """
    lista_jugadores_ordenada = ordenar_por_key(lista_jugadores, constantes.NOMBRE, ascendente)
    promedio = calcular_promedio_estadistica(estadistica, lista_jugadores)
    lista_imprimir = []
    for jugador in lista_jugadores_ordenada:
        texto = obtener_nombre_y_estadisticas(jugador, [estadistica])
        lista_imprimir.append(texto)
    estadistica_texto = estadistica.replace("_", " ")
    lista_imprimir.append(f"El promedio de {estadistica_texto} entre todos los jugadores es {promedio}")
    imprimir(lista_imprimir)

def mostrar_promedio_puntos_por_partido_ascendente(lista_jugadores):
    """
    Muestra el promedio de puntos por partido de todos los jugadores, ordenado de forma ascendente por nombre.

    Recibe:
    - lista_jugadores: Lista de diccionarios que representan a los jugadores.

    No devuelve ningún valor.
    """
    imprimir_promedio_y_estadistica(constantes.PROMEDIO_PUNTOS_POR_PARTIDO, lista_jugadores, True)

def mostrar_promedio_puntos_por_partido_excluyendo_peor(lista_jugadores):
    """
    Muestra el promedio de puntos por partido del equipo excluyendo al peor jugador.

    Recibe:
    - lista_jugadores: Lista de diccionarios que representan a los jugadores.

    No devuelve ningún valor.
    """
    lista_jugadores = ordenar_por_estadistica(lista_jugadores, constantes.PROMEDIO_PUNTOS_POR_PARTIDO)
    lista_filtrada = lista_jugadores[1:]
    promedio = get_promedio_por_clave(constantes.PROMEDIO_PUNTOS_POR_PARTIDO, lista_filtrada)
    imprimir([f"El promedio de puntos por partido del equipo excluyendo al peor jugador es {promedio}"])

def mostrar_estadisticas_y_guardar(jugadores, indice):
    """
    Muestra las estadísticas de un jugador y guarda sus datos en un archivo CSV.

    Recibe:
    - jugadores: Lista de diccionarios que representan a los jugadores.
    - indice: Índice del jugador cuyas estadísticas se mostrarán y guardarán.

    No devuelve ningún valor.
    """
    estadisticas_por_indice(jugadores, indice)
    guardar_jugador_a_csv(jugadores[indice], True)

def mostrar_jugador_con_mas_logros(lista_jugadores):
    """
    Muestra el jugador con más logros.

    Recibe:
    - lista_jugadores: Lista de diccionarios que representan a los jugadores.

    No devuelve ningún valor.
    """
    jugador = obtener_jugador_con_mas_logros(lista_jugadores)
    imprimir([f"El jugador con más logros es {jugador[constantes.NOMBRE]}, con {len(jugador[constantes.LOGROS])} logros."])

def imprimir_nombre_y_posicion_jugadores(jugadores):
    """
    Imprime los nombres y posicion de los jugadores.

    Recibe:
    - jugadores: Lista de diccionarios que representan a los jugadores.

    No devuelve ningún valor.
    """
    for jugador in jugadores:
        print(obtener_nombre_y_datos(jugador, [constantes.POSICION]))
