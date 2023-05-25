from Funciones.funciones_calcular import estadisticas_por_indice, calcular_promedio_estadistica
from Funciones.funciones_encontrar import *
from Archivos.archivos import guardar_jugador_a_csv

def imprimir_logros(jugador):
    logros = jugador["logros"]
    imprimir([jugador["nombre"]])
    imprimir(logros)


def mostrar_logros_por_nombre(lista_jugadores, nombre):
    jugadores = encontrar_jugador_por_clave(lista_jugadores, "nombre", nombre)
    if len(jugadores) == 0:
        print("No existe jugador con ese nombre.")
        return
    else:
        for jugador in jugadores:
            imprimir_logros(jugador)


def imprimir_promedio_y_estadistica(estadistica, lista_jugadores, ascendente):
    lista_jugadores_ordenada = ordenar_por_key(lista_jugadores, "nombre", ascendente)
    promedio = calcular_promedio_estadistica(estadistica, lista_jugadores)
    lista_imprimir = []
    for jugador in lista_jugadores_ordenada:
        texto = obtener_nombre_y_estadisticas(jugador, [estadistica])
        lista_imprimir.append(texto)
    lista_imprimir.append(f"El promedio de puntos promedio por partido entre todos los jugadores es {promedio}")
    imprimir(lista_imprimir)

def mostrar_promedio_puntos_por_partido_ascendente(lista_jugadores):
    imprimir_promedio_y_estadistica("promedio_puntos_por_partido", lista_jugadores, True)

def mostrar_estadisticas_y_guardar(jugadores, indice):
    estadisticas_por_indice(jugadores, indice)
    guardar_jugador_a_csv(jugadores[indice])

def obtener_nombre(jugador):
    return f"Nombre: {jugador['nombre']}"

def obtener_nombre_y_datos(jugador, lista_datos):
    linea = obtener_nombre(jugador)
    for dato in lista_datos:
        linea = f"{linea} - {obtener_dato(jugador, dato)}"
    return f"{linea}\n"

def obtener_nombre_y_estadisticas(jugador, claves):
    linea = obtener_nombre(jugador)
    for clave in claves:
        linea = f"{linea} - {obtener_dato(jugador['estadisticas'], clave)}"
    return linea

def obtener_dato(diccio, dato):
    return diccio[dato]

def imprimir(lista_elementos):
    for elemento in lista_elementos:
        print(f"{elemento}\n")

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

def imprimir_jugadores(jugadores):
    for jugador in jugadores:
        print(obtener_nombre_y_datos(jugador, ["posicion"]))
