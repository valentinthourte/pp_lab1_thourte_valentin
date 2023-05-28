from Funciones.funciones_calcular import *
from Funciones.funciones_encontrar import *
from Pantalla.imprimir import imprimir
from Archivos.archivos import guardar_jugador_a_csv

def imprimir_logros(jugador):
    logros = jugador[constantes.LOGROS]
    imprimir([jugador[constantes.NOMBRE]])
    imprimir(logros)


def mostrar_logros_por_nombre(lista_jugadores, nombre):
    jugadores = encontrar_jugadores_por_clave(lista_jugadores, constantes.NOMBRE, nombre)
    if len(jugadores) == 0:
        print("No existe jugador con ese nombre.")
        return
    else:
        for jugador in jugadores:
            imprimir_logros(jugador)

def imprimir_jugadores_y_estadisticas(lista_jugadores, estadisticas, es_porcentaje = False, agregar_posicion = False):
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
    jugadores = obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, constantes.PROMEDIO_PUNTOS_POR_PARTIDO)
    if len(jugadores) == 0:
        print("No hay jugadores que superen ese valor de promedio de puntos por partido.")
    else:
        imprimir_jugadores_y_estadisticas(jugadores, [constantes.PROMEDIO_PUNTOS_POR_PARTIDO])

def mostrar_jugadores_promedian_mas_rebotes_por_partido(lista_jugadores, valor):
    jugadores = obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, constantes.PROMEDIO_REBOTES_POR_PARTIDO)
    if len(jugadores) == 0:
        print("No hay jugadores que superen ese valor de promedio de rebotes por partido.")
    else:
        imprimir_jugadores_y_estadisticas(jugadores, [constantes.PROMEDIO_REBOTES_POR_PARTIDO])

def mostrar_jugadores_promedian_mas_asistencias_por_partido(lista_jugadores, valor):
    jugadores = obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, constantes.PROMEDIO_ASISTENCIAS_POR_PARTIDO)
    if len(jugadores) == 0:
        print("No hay jugadores que superen ese valor de promedio de asistencias por partido.")
    else:
        imprimir_jugadores_y_estadisticas(jugadores, [constantes.PROMEDIO_ASISTENCIAS_POR_PARTIDO])

def mostrar_jugadores_promedian_mas_porcentaje_tiros_libres(lista_jugadores, valor):
    jugadores = obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, constantes.PORCENTAJE_TIROS_LIBRES)
    if len(jugadores) == 0:
        print("No hay jugadores que superen ese porcentaje de tiros libres.")
    else:
        imprimir_jugadores_y_estadisticas(jugadores, [constantes.PORCENTAJE_TIROS_LIBRES], True)

def mostrar_jugadores_promedian_mas_porcentaje_tiros_triples(lista_jugadores, valor):
    jugadores = obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, constantes.PORCENTAJE_TIROS_TRIPLES)
    if len(jugadores) == 0:
        print("No hay jugadores que superen ese porcentaje de tiros triples.")
    else:
        imprimir_jugadores_y_estadisticas(jugadores, [constantes.PORCENTAJE_TIROS_TRIPLES], True)

def mostrar_jugadores_promedian_mas_porcentaje_tiros_campo_por_posicion(lista_jugadores, valor):
    jugadores = obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, constantes.PORCENTAJE_TIROS_DE_CAMPO)
    if len(jugadores) == 0:
        print("No hay jugadores que superen ese porcentaje de tiros de campo.")
    else:
        jugadores = ordenar_por_key(jugadores, constantes.POSICION, True)
        imprimir_jugadores_y_estadisticas(jugadores, [constantes.PORCENTAJE_TIROS_DE_CAMPO], True, True)

def guardar_ranking_jugadores(lista_jugadores, lista_rankings):
    diccio_ranking = obtener_jugadores_rankeados_por_estadisticas(lista_jugadores, lista_rankings)

def mostrar_jugador_mas_temporadas_jugadas(lista_jugadores):
    jugador = obtener_jugador_mas_temporadas_jugadas(lista_jugadores)
    imprimir([obtener_nombre_y_estadisticas(jugador, [constantes.TEMPORADAS])])

def mostrar_jugador_mayor_rebotes_totales(lista_jugadores):
    jugador = obtener_jugador_mayor_rebotes_totales(lista_jugadores)
    imprimir([obtener_nombre_y_estadisticas(jugador, [constantes.REBOTES_TOTALES])])

def mostrar_jugador_mayor_porcentaje_tiros_campo(lista_jugadores):
    jugador = obtener_jugador_mayor_porcentaje_tiros_campo(lista_jugadores)
    imprimir([f"{obtener_nombre_y_estadisticas(jugador, [constantes.PORCENTAJE_TIROS_DE_CAMPO])}%"])

def mostrar_jugador_mayor_robos_totales(lista_jugadores):
    jugador = obtener_jugador_mayor_robos_totales(lista_jugadores)
    imprimir([obtener_nombre_y_estadisticas(jugador, [constantes.ROBOS_TOTALES])])

def mostrar_jugador_mayor_bloqueos_totales(lista_jugadores):
    jugador = obtener_jugador_mayor_bloqueos_totales(lista_jugadores)
    imprimir([obtener_nombre_y_estadisticas(jugador, [constantes.BLOQUEOS_TOTALES])])


def mostrar_jugador_mayor_asistencias(lista_jugadores):
    jugador = obtener_jugador_mayor_asistencias(lista_jugadores)
    imprimir([obtener_nombre_y_estadisticas(jugador, [constantes.ASISTENCIAS_TOTALES])])


def imprimir_promedio_y_estadistica(estadistica, lista_jugadores, ascendente):
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
    imprimir_promedio_y_estadistica(constantes.PROMEDIO_PUNTOS_POR_PARTIDO, lista_jugadores, True)

def mostrar_promedio_puntos_por_partido_excluyendo_peor(lista_jugadores):
    lista_jugadores = ordenar_por_estadistica(lista_jugadores, constantes.PROMEDIO_PUNTOS_POR_PARTIDO, True)
    lista_filtrada = lista_jugadores[1:]
    promedio = get_promedio_por_clave(constantes.PROMEDIO_PUNTOS_POR_PARTIDO,lista_filtrada)
    imprimir([f"El promedio de puntos por partido del equipo excluyendo al peor jugador es {promedio}"])

def mostrar_estadisticas_y_guardar(jugadores, indice):
    estadisticas_por_indice(jugadores, indice)
    guardar_jugador_a_csv(jugadores[indice])

def mostrar_jugador_con_mas_logros(lista_jugadores):
    jugador = obtener_jugador_con_mas_logros(lista_jugadores)
    imprimir([f"El jugador con mas logros es {jugador[constantes.NOMBRE]}, con {len(jugador[constantes.LOGROS])} logros."])


def imprimir_jugadores(jugadores):
    for jugador in jugadores:
        print(obtener_nombre_y_datos(jugador, [constantes.POSICION]))
