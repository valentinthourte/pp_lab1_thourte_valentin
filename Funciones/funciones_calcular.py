from Pantalla.imprimir import imprimir
import constantes

def ordenar_por_key(lista, clave, ascendente):
    ordenar = True
    while ordenar:
        ordenar = False
        for i in range(len(lista) - 1):
            actual = lista[i]
            proximo = lista[i+ 1]
            if (actual[clave] > proximo[clave]) == ascendente:
                lista[i] = proximo
                lista[i + 1] = actual
                ordenar = True
    return lista

def ordenar_por_estadistica(lista, clave, ascendente):
    ordenar = True
    while ordenar:
        ordenar = False
        for i in range(len(lista) - 1):
            actual = lista[i]
            proximo = lista[i+ 1]
            if (actual[constantes.ESTADISTICAS][clave] > proximo[constantes.ESTADISTICAS][clave]) == ascendente:
                lista[i] = proximo
                lista[i + 1] = actual
                ordenar = True
    return lista

def obtener_nombre(jugador):
    return f"Nombre: {jugador[constantes.NOMBRE]}"

def obtener_nombre_y_datos(jugador, lista_datos):
    linea = obtener_nombre(jugador)
    for dato in lista_datos:
        linea = f"{linea} - {obtener_dato(jugador, dato)}"
    return f"{linea}\n"

def obtener_nombre_y_estadisticas(jugador, claves):
    linea = obtener_nombre(jugador)
    for clave in claves:
        linea = f"{linea} - {clave_y_estadistica_parseadas(jugador, clave)}"
    return linea

def obtener_dato(diccio, dato):
    return diccio[dato]

def obtener_clave_y_dato(diccio, dato):
    return f"{parsear_dato(dato)}: {obtener_dato(diccio, dato)}"

def clave_y_estadistica_parseadas(jugador, clave):
    dato = obtener_dato(jugador[constantes.ESTADISTICAS], clave)
    clave_parseada = parsear_dato(clave)
    return f"{clave_parseada}: {dato}"

def parsear_dato(estadistica):
    return estadistica.replace("_", " ").capitalize()

def get_promedio_por_clave(clave, lista):
    if len(lista) == 0:
        return 0
    else:
        suma = 0
        for jugador in lista:
            suma += float(jugador[constantes.ESTADISTICAS][clave])
        return suma / len(lista)
    

def get_jugador_mas_por_clave(clave, lista):
    for i in range(len(lista) - 1):
        jugador = lista[i]
        if i == 0:
            jugador_mas = jugador
        else:
            if float(jugador[constantes.ESTADISTICAS][clave]) > float(jugador_mas[constantes.ESTADISTICAS][clave]):
                jugador_mas = jugador
    return jugador_mas


def get_jugador_menos_por_clave(clave, lista):
    for i in range(len(lista) - 1):
        jugador = lista[i]
        if i == 0:
            jugador_menos = jugador
        else:
            if float(jugador[constantes.ESTADISTICAS][clave]) < float(jugador_menos[constantes.ESTADISTICAS][clave]):
                jugador_menos = jugador
    return jugador_menos

def get_jugador_mas_longitud_clave(lista_jugadores, clave):
    for i in range(len(lista_jugadores) - 1):
        jugador = lista_jugadores[i]
        if i == 0:
            jugador_mas = jugador
        else:
            if len(jugador[clave]) > len(jugador_mas[clave]):
                jugador_mas = jugador
    return jugador_mas

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

def obtener_jugador_con_mas_logros(lista_jugadores):
    return get_jugador_mas_longitud_clave(lista_jugadores, constantes.LOGROS)

def estadisticas_por_indice(jugadores, indice):
    jugador = jugadores[indice]
    nombre_jugador = jugador[constantes.NOMBRE]
    estadisticas = parsear_estadisticas(jugador[constantes.ESTADISTICAS])
    imprimir([nombre_jugador, estadisticas])

def obtener_jugador_mas_temporadas_jugadas(lista_jugadores):
    return calcular_max_estadistica(constantes.TEMPORADAS, lista_jugadores)

def obtener_jugador_mayor_bloqueos_totales(lista_jugadores):
    return calcular_max_estadistica(constantes.BLOQUEOS_TOTALES, lista_jugadores)

def obtener_jugador_mayor_robos_totales(lista_jugadores):
    return calcular_max_estadistica(constantes.ROBOS_TOTALES, lista_jugadores)

def obtener_jugador_mayor_rebotes_totales(lista_jugadores):
    return calcular_max_estadistica(constantes.REBOTES_TOTALES, lista_jugadores)

def obtener_jugador_mayor_porcentaje_tiros_campo(lista_jugadores):
    return calcular_max_estadistica(constantes.PORCENTAJE_TIROS_DE_CAMPO, lista_jugadores)

def obtener_jugador_mayor_asistencias(lista_jugadores):
    return calcular_max_estadistica(constantes.ASISTENCIAS_TOTALES, lista_jugadores)

def obtener_jugadores_mas_puntos_partido_que_promedio(lista_jugadores, valor):
    return obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, constantes.PROMEDIO_PUNTOS_POR_PARTIDO)

def obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, estadistica):
    return obtener_jugadores_comparados_estadistica(lista_jugadores, valor, estadistica, True)

def obtener_jugadores_comparados_estadistica(lista_jugadores, valor, estadistica, mayor):
    jugadores_devolver = []
    for jugador in lista_jugadores:
        if (jugador[constantes.ESTADISTICAS][estadistica] >= valor) == mayor:
            jugadores_devolver.append(jugador)
    return jugadores_devolver

def obtener_jugadores_rankeados_por_estadisticas(lista_jugadores, lista_rankings):

    for estadistica in lista_rankings:
        lista_ordenada = ordenar_por_estadistica(lista_jugadores, estadistica, True)
        for i in range (len(lista_ordenada) - 1):
            jugador = lista_ordenada[i]
            if not constantes.RANKINGS in jugador:
                jugador[constantes.RANKINGS] = {}
            jugador[constantes.RANKINGS][estadistica] = i

