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
        archivo (str): El nombre del archivo a leer

    Returns:
        list: Una lista de diccionarios que contiene la información de los jugadores leída desde el archivo.
    """
    nombre_archivo = f"{archivo}.json"
    with open(nombre_archivo, "r", encoding="utf-8") as archivo_json:
        data = json.load(archivo_json)
    return data["jugadores"]

def sanitizar(texto):
    """
    Reemplaza las comas por puntos y coma (;) y las nuevas líneas por arrobas (@) en un texto.

    Args:
        texto (str): El texto a sanitizar.

    Returns:
        str: El texto sanitizado.
    """
    if type(texto) != str:
        return texto
    else:
        return texto.replace(",", ";").replace("\n", "@")

def parse_jugador_a_csv(jugador, clave_guardar, incluir_posicion = True):
    """
    Convierte la información de un jugador en una línea CSV para ser guardada en un archivo.

    Recibe:
    - jugador: Diccionario que representa al jugador.
    - clave_guardar: La clave correspondiente a las estadísticas a guardar.

    Devuelve:
    - Cadena de texto que representa la línea CSV del jugador.
    """
    linea_csv = f"{jugador[constantes.NOMBRE]},"
    if incluir_posicion:
        linea_csv += f"{jugador[constantes.POSICION]},"
    claves = jugador[clave_guardar]
    for clave in claves:
        clave_sanitizada = sanitizar(claves[clave])
        linea_csv = f"{linea_csv}{clave_sanitizada},"
    return f"{linea_csv[:-1]}\n"

def guardar_jugador_a_csv(jugador, usar_jugador_para_archivo=False):
    """
    Guarda la información de un jugador en un archivo CSV.

    Recibe:
    - jugador: Diccionario que representa al jugador.
    - usar_jugador_para_archivo: Booleano que indica si se usará el nombre y apellido del jugador para el nombre del archivo.

    No devuelve ningún valor.
    """
    nombre_archivo = nombre_archivo_para_csv(jugador, usar_jugador_para_archivo)
    grabar_cabeceras = not os.path.exists(nombre_archivo)
    with open(nombre_archivo, "a") as archivo:
        if grabar_cabeceras:
            linea_cabeceras = obtener_cabeceras_de_jugador(jugador)
            archivo.write(linea_cabeceras)
        linea = parse_jugador_a_csv(jugador, constantes.ESTADISTICAS)
        archivo.write(linea)

def obtener_cabeceras_de_jugador(jugador):
    """
    Obtiene las cabeceras para el archivo CSV basadas en las claves del diccionario de jugador.

    Recibe:
    - jugador: Diccionario que representa al jugador.

    Devuelve:
    - Cadena de texto que representa las cabeceras para el archivo CSV.
    """
    linea = ""
    for clave in jugador:
        if type(jugador[clave]) == dict:
            for elemento in jugador[clave]:
                linea = f"{linea},{elemento}"
        else:
            linea = f"{linea},{clave}"
    return f"{linea[1:]}\n"

def obtener_nombre_y_apellido(jugador):
    """
    Obtiene el nombre y apellido de un jugador.

    Recibe:
    - jugador: Diccionario que representa al jugador.

    Devuelve:
    - Tupla que contiene el nombre y apellido del jugador.
    """
    lista = jugador["nombre"].split(" ")
    return lista[0], lista[-1]

def nombre_archivo_para_csv(jugador, usar_jugador_para_archivo):
    """
    Genera el nombre del archivo CSV para guardar las estadísticas de un jugador.

    Recibe:
    - jugador: Diccionario que representa al jugador.
    - usar_jugador_para_archivo: Booleano que indica si se usará el nombre y apellido del jugador para el nombre del archivo.

    Devuelve:
    - Cadena de texto que representa el nombre del archivo CSV.
    """
    if usar_jugador_para_archivo:
        nombre, apellido = obtener_nombre_y_apellido(jugador)
        nombre_archivo = f"estadisticas_{nombre}_{apellido}.csv"
    else:
        nombre_archivo = "estadisticas.csv"
    return nombre_archivo

def guardar_rankings_a_csv(diccio_ranking, lista_rankings):
    """
    Guarda los rankings en un archivo CSV.

    Recibe:
    - diccio_ranking: Diccionario que contiene los rankings de los jugadores.
    - lista_rankings: Lista de los nombres de los rankings.

    No devuelve ningún valor.
    """
    lista_rankings = sanitizar_lista(lista_rankings)
    cabeceras = f"Nombre,{','.join(lista_rankings)}"
    with open("rankings.csv", "w") as archivo:
        archivo.write(f"{cabeceras}\n")
        for jugador in diccio_ranking:
            linea = parse_jugador_a_csv(jugador, constantes.RANKINGS, False)
            archivo.write(linea)

def sanitizar_lista(lista):
    """
    Sanitiza los elementos de una lista.

    Recibe:
    - lista: Lista de elementos a sanitizar.

    Devuelve:
    - Lista con los elementos sanitizados.
    """
    for i in range(len(lista)):
        lista[i] = sanitizar(parsear_dato(lista[i]))
    return lista
