import json
import re
import os

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
    "0. Salir"
    ]
    imprimir_menu(lista_opciones)
    return len(lista_opciones)

def validar_opcion(opcion, cantidad_opciones):
    """
    Función que recibe una opción y valida si cumple con el patrón de una letra de la A a la O.

    :param opcion: opción que se desea validar.
    :return: la opción si cumple con el patrón de una letra de la A a la O, -1 si no cumple con el patrón.
    """
    patron = r"^[0-9]{1,2}$"
    ocurrencias = re.findall(patron, opcion)
    if len(ocurrencias) == 0 or (int(ocurrencias[0]) > cantidad_opciones or int(ocurrencias[0]) < 0):
        return -1
    return opcion

def imprimir_menu(lista):
    for opcion in lista:
        imprimir([opcion])

def menu_principal(texto_input):
    cantidad_opciones = imprimir_menu_parcial()
    opcion = input(texto_input)
    return validar_opcion(opcion, cantidad_opciones)

def pedir_opcion_hasta__que_sea_valida(texto_input = "Ingrese una opción para continuar: "):
    opcion = menu_principal(texto_input)
    while opcion == -1:
        opcion = menu_principal(texto_input)
    return int(opcion)


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

def mostrar_estadisticas_y_guardar(jugadores, indice):
    estadisticas_por_indice(jugadores, indice)
    guardar_jugador_a_csv(jugadores[indice])

def parse_jugador_a_csv(jugador):
    linea_csv = f"{jugador['nombre']},{jugador['posicion']},"
    estadisticas = jugador["estadisticas"]
    for estadistica in estadisticas:
        estadistica_sanitizada = sanitizar(estadisticas[estadistica])
        linea_csv = f"{linea_csv}{estadistica_sanitizada},"
    return f"{linea_csv[:-1]}\n"

def obtener_cabeceras_de_jugador(jugador):
    linea = ""
    for clave in jugador:
        linea = f"{linea},{clave}"
    return f"{linea}\n"

def guardar_jugador_a_csv(jugador):
    nombre_archivo = "estadisticas.csv"
    grabar_cabeceras = not os.path.exists(nombre_archivo)
    with open(nombre_archivo, "a") as archivo:
        if grabar_cabeceras:
            linea_cabeceras = obtener_cabeceras_de_jugador(jugador)
            archivo.write(linea_cabeceras)
        linea = parse_jugador_a_csv(jugador)
        archivo.write(linea)

def imprimir_logros(jugador):
    logros = jugador["logros"]
    imprimir([jugador["nombre"]])
    imprimir(logros)

def encontrar_jugador_por_clave(lista_jugadores, clave, valor):
    jugadores_coincidencia = []
    for jugador in lista_jugadores:
        contiene = jugador[clave].lower().startswith(valor.lower())
        if contiene:
            jugadores_coincidencia.append(jugador)

    return jugadores_coincidencia

def mostrar_logros_por_nombre(lista_jugadores, nombre):
    jugadores = encontrar_jugador_por_clave(lista_jugadores, "nombre", nombre)
    if len(jugadores) == 0:
        print("No existe jugador con ese nombre.")
        return
    else:
        for jugador in jugadores:
            imprimir_logros(jugador)

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

def imprimir_promedio_y_estadistica(estadistica, lista_jugadores, ascendente):
    lista_jugadores_ordenada = ordenar_por_key(lista_jugadores, "nombre", ascendente)

def mostrar_promedio_puntos_por_partido_ascendente(lista_jugadores):
    lista_puntos = []
    lista_jugadores_ordenada = ordenar_por_key(lista_jugadores, "nombre", True)
    for jugador in lista_jugadores_ordenada:
        texto = f"{obtener_nombre(jugador)} - {obtener_dato(jugador['estadisticas'], 'promedio_puntos_por_partido')}"
        lista_puntos.append(texto)
    imprimir(lista_puntos)

def jugador_es_parte_dream_team(lista_jugadores, nombre):
    jugador = encontrar_jugador_por_clave(lista_jugadores, "nombre", nombre)
    return jugador != None

def obtener_jugador_mayor_rebotes_totales(lista_jugadores):
    return calcular_max_estadistica("rebotes_totales", lista_jugadores)

def obtener_jugador_mayor_porcentaje_tiros_campo(lista_jugadores):
    return calcular_max_estadistica("porcentaje_tiros_de_campo", lista_jugadores)

def obtener_jugador_mayor_asistencias(lista_jugadores):
    return calcular_max_estadistica("asistencias_totales", lista_jugadores)

def validar_indice(indice, cantidad_jugadores):
    indice = str(int(indice) - 1)
    patron = r"^[0-9]+$"
    ocurrencias = re.findall(patron, indice)
    if len(ocurrencias) == 0 or int(ocurrencias[0]) >= cantidad_jugadores:
        indice = input(f"Ingrese un índice válido, numérico positivo menor o igual a {cantidad_jugadores}: ")
        return validar_indice(indice, cantidad_jugadores)
    else:
        return int(indice)

