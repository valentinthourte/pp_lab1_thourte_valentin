from Funciones.funciones_mostrar import *

def get_promedio_por_clave(clave, lista):
    if len(lista) == 0:
        return 0
    else:
        suma = 0
        for jugador in lista:
            suma += float(jugador["estadisticas"][clave])
        return suma / len(lista)
    

def get_jugador_mas_por_clave(clave, lista):
    for i in range(len(lista) - 1):
        jugador = lista[i]
        if i == 0:
            jugador_mas = jugador
        else:
            if float(jugador["estadisticas"][clave]) > float(jugador_mas["estadisticas"][clave]):
                jugador_mas = jugador
    return jugador_mas


def get_jugador_menos_por_clave(clave, lista):
    for i in range(len(lista) - 1):
        jugador = lista[i]
        if i == 0:
            jugador_menos = jugador
        else:
            if float(jugador["estadisticas"][clave]) < float(jugador_menos["estadisticas"][clave]):
                jugador_menos = jugador
    return jugador_menos

def calcular_max_estadistica(clave, lista_jugadores):
    return get_jugador_mas_por_clave(clave, lista_jugadores)

def calcular_min_estadistica(clave, lista_jugadores):
    return get_jugador_menos_por_clave(clave, lista_jugadores)

def calcular_promedio_estadistica(clave, lista_jugadores):
    return get_promedio_por_clave(clave, lista_jugadores)   


def parsear_estadisticas(estadisticas):
    linea = ""
    for clave in estadisticas:
        clave_parseada = clave.capitalize().replace("_", " ")
        linea = f"{linea} {clave_parseada}: {estadisticas[clave]} |"
    return linea

def estadisticas_por_indice(jugadores, indice):
    jugador = jugadores[indice]
    nombre_jugador = jugador["nombre"]
    estadisticas = parsear_estadisticas(jugador["estadisticas"])
    imprimir([nombre_jugador, estadisticas])

def obtener_jugador_mayor_rebotes_totales(lista_jugadores):
    return calcular_max_estadistica("rebotes_totales", lista_jugadores)

def obtener_jugador_mayor_porcentaje_tiros_campo(lista_jugadores):
    return calcular_max_estadistica("porcentaje_tiros_de_campo", lista_jugadores)

def obtener_jugador_mayor_asistencias(lista_jugadores):
    return calcular_max_estadistica("asistencias_totales", lista_jugadores)
