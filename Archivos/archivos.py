from Funciones.funciones_calcular import *
import os
import json
def leer_archivo(nombre_archivo, extension_archivo):
    """
    Lee un archivo con formato JSON o CSV y devuelve su contenido.

    Args:
        nombre_archivo (str): El nombre del archivo a leer (sin la extensión).
        extension_archivo (str): La extensión del archivo (json o csv).

    Returns:
        list: Una lista de diccionarios que contiene la información de los jugadores leída desde el archivo.
    """
    match extension_archivo:
        case "json":
            return parse_json(nombre_archivo)
        case _:
            return []


def parse_json(archivo):
    """
    Lee un archivo en formato JSON y devuelve la información de los jugadores.

    Args:
        archivo (str): El nombre del archivo a leer (incluyendo la extensión).

    Returns:
        list: Una lista de diccionarios que contiene la información de los jugadores leída desde el archivo.
    """
    nombre_archivo = f"{archivo}.json"
    with open(nombre_archivo, "r") as archivo_json:
        data = json.load(archivo_json)
    return data["jugadores"]

def sanitizar(texto):
    """
    Reemplaza las comas por puntos y coma (;) y las nuevas líneas por arrobas (@) en un texto.

    Args:
        texto (str): El texto a sanizar.

    Returns:
        str: El texto sanizado.
    """
    if type(texto) != str:
        return texto
    else:
        return texto.replace(",", ";").replace("\n", "@")
    

def parse_jugador_a_csv(jugador):
    linea_csv = f"{jugador['nombre']},{jugador['posicion']},"
    estadisticas = jugador["estadisticas"]
    for estadistica in estadisticas:
        estadistica_sanitizada = sanitizar(estadisticas[estadistica])
        linea_csv = f"{linea_csv}{estadistica_sanitizada},"
    return f"{linea_csv[:-1]}\n"

def guardar_jugador_a_csv(jugador, usar_jugador_para_archivo = False):
    nombre_archivo = nombre_archivo_para_csv(jugador, usar_jugador_para_archivo)
    grabar_cabeceras = not os.path.exists(nombre_archivo)
    with open(nombre_archivo, "a") as archivo:
        if grabar_cabeceras:
            linea_cabeceras = obtener_cabeceras_de_jugador(jugador)
            archivo.write(linea_cabeceras)
        linea = parse_jugador_a_csv(jugador)
        archivo.write(linea)

def obtener_cabeceras_de_jugador(jugador):
    linea = ""
    for clave in jugador:
        linea = f"{linea},{clave}"
    return f"{linea}\n"

def obtener_nombre_y_apellido(jugador):
    lista = jugador["nombre"].split(" ")
    return lista[0], lista[1]

def nombre_archivo_para_csv(jugador, usar_jugador_para_archivo):
    if usar_jugador_para_archivo:
        nombre, apellido = obtener_nombre_y_apellido(jugador)
        nombre_archivo = f"estadisticas_{nombre}_{apellido}.csv"
    else:
        nombre_archivo = "estadisticas.csv"
    return nombre_archivo