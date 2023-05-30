from Pantalla.imprimir import imprimir
from Funciones.funciones_encontrar import encontrar_jugadores_por_clave
import constantes
import re


def ordenar(lista, clave, logica, ascendente):
    """
    Ordena una lista de diccionarios por una clave específica.

    Parámetros:
        lista (list): La lista de diccionarios a ordenar.
        clave (str): La clave por la cual se va a ordenar la lista.
        logica(func): La funcion a ejecutar para determinar si corresponde intercambiar elementos 
        ascendente (bool, optional): Indica si se debe ordenar de forma ascendente (True) o descendente (False). 
            Por defecto es True.

    Returns:
        list: La lista ordenada por la clave especificada.
    """
    ordenar = True
    while ordenar:
        ordenar = False
        for i in range(len(lista) - 1):
            actual = lista[i]
            proximo = lista[i+1]
            if logica(actual, proximo, clave, ascendente) == ascendente:
                lista[i] = proximo
                lista[i + 1] = actual
                ordenar = True
    return lista

def obtener_mejor_por_estadistica(estadistica, lista_jugadores):
    ordenada = ordenar_por_estadistica(lista_jugadores, estadistica, False)
    return ordenada[0]

def obtener_mejores(lista_jugadores):
    mejores = []
    for estadistica in constantes.LISTA_ESTADISTICAS:
        mejor = obtener_mejor_por_estadistica(estadistica, lista_jugadores)
        diccio_mejor = {
            constantes.NOMBRE: mejor[constantes.NOMBRE],
            constantes.CLAVE_MEJOR_EN: estadistica,
            constantes.CLAVE_CANTIDAD_MEJOR: mejor[constantes.ESTADISTICAS][estadistica],
        }
        mejores.append(diccio_mejor)
    return mejores

def ordenar_por_key(lista, clave, ascendente=True):
    """
    Ordena una lista de diccionarios por una clave específica.

    Parámetros:
        lista (list): La lista de diccionarios a ordenar.
        clave (str): La clave por la cual se va a ordenar la lista.
        ascendente (bool, optional): Indica si se debe ordenar de forma ascendente (True) o descendente (False). 
            Por defecto es True.

    Returns:
        list: La lista ordenada por la clave especificada.
    """
    def logica_por_key(actual, proximo, clave, ascendente):
        if actual[clave] == proximo[clave]:
            return not ascendente
        return actual[clave] > proximo[clave]
    
    return ordenar(lista, clave, logica_por_key, ascendente)


def ordenar_por_estadistica(lista, clave, ascendente=True):
    """
    Ordena una lista de diccionarios por una estadística específica.

    Parámetros:
        lista (list): La lista de diccionarios a ordenar.
        clave (str): La clave de la estadística por la cual se va a ordenar la lista.
        ascendente (bool, optional): Indica si se debe ordenar de forma ascendente (True) o descendente (False). 
            Por defecto es True.

    Returns:
        list: La lista ordenada por la estadística especificada.
    """
    def logica_por_estadistica(actual, proximo, clave, ascendente):
        if actual[constantes.ESTADISTICAS][clave] == proximo[constantes.ESTADISTICAS][clave]:
            return not ascendente
        return actual[constantes.ESTADISTICAS][clave] > proximo[constantes.ESTADISTICAS][clave]
    return ordenar(lista, clave, logica_por_estadistica, ascendente)    

def ordenar_por_posicion_cancha(lista, clave, ascendente=True):
    def logica_por_posicion(actual, proximo, clave, ascendente):
        if constantes.LISTA_POSICIONES.index(actual[clave]) == constantes.LISTA_POSICIONES.index(proximo[clave]):
            return not ascendente
        return constantes.LISTA_POSICIONES.index(actual[clave]) > constantes.LISTA_POSICIONES.index(proximo[clave])
    return ordenar(lista, clave, logica_por_posicion, ascendente)

def obtener_nombre(jugador):
    """
    Obtiene el nombre de un jugador.

    Parámetros:
        jugador (dict): El diccionario que representa al jugador.

    Returns:
        str: El nombre del jugador.
    """
    return f"Nombre: {jugador[constantes.NOMBRE]}"


def obtener_nombre_y_datos(jugador, lista_datos):
    """
    Obtiene el nombre de un jugador y los datos asociados a partir de una lista de datos.

    Parámetros:
        jugador (dict): El diccionario que representa al jugador.
        lista_datos (list): La lista de datos a obtener.

    Returns:
        str: Una cadena que contiene el nombre del jugador y los datos solicitados.
    """
    linea = obtener_nombre(jugador)
    for dato in lista_datos:
        linea = f"{linea} - {obtener_dato(jugador, dato)}"
    return f"{linea}\n"

def obtener_nombre_y_rankings(jugador, rankings):
    """
    Obtiene el nombre de un jugador y los rankings asociados a él.

    Parámetros:
    - jugador (dict): El diccionario que representa al jugador.
    - rankings (list): La lista de rankings a obtener.

    Retorna:
    - str: Una cadena de texto que contiene el nombre del jugador y los rankings asociados en el formato "Nombre: {nombre} - {ranking1}: {valor1} - {ranking2}: {valor2} ...".

    """
    linea = obtener_nombre(jugador)
    for ranking in rankings:
        linea = f"{linea} - {clave_y_ranking_parseadas(jugador, ranking)}"
    return linea


def obtener_nombre_y_estadisticas(jugador, claves):
    """
    Obtiene el nombre de un jugador y las estadísticas asociadas a él.

    Parámetros:
    - jugador (dict): El diccionario que representa al jugador.
    - claves (list): La lista de claves de las estadísticas a obtener.

    Retorna:
    - str: Una cadena de texto que contiene el nombre del jugador y las estadísticas asociadas en el formato "Nombre: {nombre} - {estadistica1}: {valor1} - {estadistica2}: {valor2} ...".

    """
    linea = obtener_nombre(jugador)
    for clave in claves:
        linea = f"{linea} - {clave_y_estadistica_parseadas(jugador, clave)}"
    return linea


def obtener_dato(diccio, dato):
    """
    Obtiene un dato específico de un diccionario.

    Parámetros:
    - diccio (dict): El diccionario del cual se desea obtener el dato.
    - dato (str): La clave del dato a obtener.

    Retorna:
    - str: El valor correspondiente al dato en el diccionario.

    """
    return diccio[dato]


def obtener_clave_y_dato(diccio, dato):
    """
    Obtiene una clave y su correspondiente dato de un diccionario.

    Parámetros:
    - diccio (dict): El diccionario del cual se desea obtener la clave y el dato.
    - dato (str): La clave del dato a obtener.

    Retorna:
    - str: Una cadena de texto en el formato "{clave_parseada}: {valor}".

    """
    return f"{parsear_dato(dato)}: {obtener_dato(diccio, dato)}"


def clave_y_estadistica_parseadas(jugador, clave):
    """
    Obtiene una clave de estadística parseada y su correspondiente valor de un jugador.

    Parámetros:
    - jugador (dict): El diccionario que representa al jugador.
    - clave (str): La clave de la estadística a obtener.

    Retorna:
    - str: Una cadena de texto en el formato "{clave_parseada}: {valor}".

    """
    dato = obtener_dato(jugador[constantes.ESTADISTICAS], clave)
    clave_parseada = parsear_dato(clave)
    return f"{clave_parseada}: {dato}"


def clave_y_ranking_parseadas(jugador, clave):
    """
    Obtiene una clave de ranking parseada y su correspondiente valor de un jugador.

    Parámetros:
    - jugador (dict): El diccionario que representa al jugador.
    - clave (str): La clave del ranking a obtener.

    Retorna:
    - str:Una cadena de texto en el formato "{clave_parseada}: {valor}".

    """
    dato = obtener_dato(jugador[constantes.RANKINGS], clave)
    clave_parseada = parsear_dato(clave)
    return f"{clave_parseada}: {dato}"

def agregar_clave_y_valor(lista, clave, valor):
    for elemento in lista:
        elemento[clave] = valor
    return lista

def obtener_mejor_estadisticamente(lista_jugadores):
    mejores = obtener_mejores(lista_jugadores)
    lista_jugadores_modificados = agregar_clave_y_valor(lista_jugadores, constantes.CLAVE_CANTIDAD_ESTADISTICAS_MEJOR, 0)
    for mejor in mejores:
        jugador = encontrar_jugadores_por_clave(lista_jugadores, constantes.NOMBRE, mejor[constantes.NOMBRE])[0]
        jugador[constantes.CLAVE_CANTIDAD_ESTADISTICAS_MEJOR] += 1
    ordenados =  ordenar_por_key(lista_jugadores_modificados, constantes.CLAVE_CANTIDAD_ESTADISTICAS_MEJOR, False)
    return ordenados[0]

def parsear_dato(estadistica):
    """
    Parsea una cadena de texto reemplazando los guiones bajos por espacios y capitalizando la primera letra.

    Parámetros:
    - estadistica (str): La cadena de texto a parsear.

    Retorna:
    - str: La cadena de texto parseada.

    """
    return estadistica.replace("_", " ").capitalize()


def get_promedio_por_clave(clave, lista):
    """
    Calcula el promedio de una clave específica en una lista de jugadores.

    Parámetros:
    - clave (str): La clave de la estadística a calcular el promedio.
    - lista (list): La lista de jugadores.

    Retorna:
    - float: El promedio de la clave en la lista de jugadores. Si la lista está vacía, retorna 0.

    """
    if len(lista) == 0:
        return 0
    else:
        suma = 0
        for jugador in lista:
            suma += float(jugador[constantes.ESTADISTICAS][clave])
        return suma / len(lista)


def get_jugador_mas_por_clave(clave, lista):
    """
    Obtiene el jugador con el valor más alto de una clave específica en una lista de jugadores.

    Parámetros:
    - clave (str): La clave de la estadística a comparar.
    - lista (list): La lista de jugadores.

    Retorna:
    - dict: El diccionario del jugador con el valor más alto de la clave.

    """
    for i in range(len(lista)):
        jugador = lista[i]
        if i == 0:
            jugador_mas = jugador
        else:
            if float(jugador[constantes.ESTADISTICAS][clave]) > float(jugador_mas[constantes.ESTADISTICAS][clave]):
                jugador_mas = jugador
    return jugador_mas


def get_jugador_menos_por_clave(clave, lista):
    """
    Obtiene el jugador con el valor más bajo de una clave específica en una lista de jugadores.

    Parámetros:
    - clave (str): La clave de la estadística a comparar.
    - lista (list): La lista de jugadores.

    Retorna:
    - dict: El diccionario del jugador con el valor más bajo de la clave.

    """
    for i in range(len(lista)):
        jugador = lista[i]
        if i == 0:
            jugador_menos = jugador
        else:
            if float(jugador[constantes.ESTADISTICAS][clave]) < float(jugador_menos[constantes.ESTADISTICAS][clave]):
                jugador_menos = jugador
    return jugador_menos

def get_jugador_mas_longitud_clave(lista_jugadores, clave):
    """
    Obtiene el jugador con el valor más largo en una clave específica de una lista de jugadores.

    Parámetros:
    - lista_jugadores (list): La lista de jugadores.
    - clave (str): La clave a comparar.

    Retorna:
    - dict: El diccionario del jugador con el valor más largo en la clave especificada.

    """
    for i in range(len(lista_jugadores)):
        jugador = lista_jugadores[i]
        if i == 0:
            jugador_mas = jugador
        else:
            if len(jugador[clave]) > len(jugador_mas[clave]):
                jugador_mas = jugador
    return jugador_mas


def calcular_max_estadistica(clave, lista_jugadores):
    """
    Calcula el jugador con el valor más alto de una clave específica en una lista de jugadores.

    Parámetros:
    - clave (str): La clave de la estadística a calcular el máximo.
    - lista_jugadores (list): La lista de jugadores.

    Retorna:
    - dict: El diccionario del jugador con el valor más alto de la clave.

    """
    return get_jugador_mas_por_clave(clave, lista_jugadores)


def calcular_min_estadistica(clave, lista_jugadores):
    """
    Calcula el jugador con el valor más bajo de una clave específica en una lista de jugadores.

    Parámetros:
    - clave (str): La clave de la estadística a calcular el mínimo.
    - lista_jugadores (list): La lista de jugadores.

    Retorna:
    - dict: El diccionario del jugador con el valor más bajo de la clave.

    """
    return get_jugador_menos_por_clave(clave, lista_jugadores)


def calcular_promedio_estadistica(clave, lista_jugadores):
    """
    Calcula el promedio de una clave específica en una lista de jugadores.

    Parámetros:
    - clave (str): La clave de la estadística a calcular el promedio.
    - lista_jugadores (list): La lista de jugadores.

    Retorna:
    - float: El promedio de la clave en la lista de jugadores. Si la lista está vacía, retorna 0.

    """
    return get_promedio_por_clave(clave, lista_jugadores)


def parsear_estadisticas(estadisticas):
    """
    Parsea un diccionario de estadísticas en una cadena de texto.

    Parámetros:
    - estadisticas (dict): El diccionario de estadísticas a parsear.

    Retorna:
    - str: Una cadena de texto en el formato "{clave_parseada}: {valor} | {clave_parseada}: {valor} ...".

    """
    linea = ""
    for clave in estadisticas:
        clave_parseada = parsear_clave(clave)
        linea = f"{linea} {clave_parseada}: {estadisticas[clave]} |"
    return linea


def parsear_clave(clave):
    return clave.capitalize().replace("_", " ")

def obtener_jugador_con_mas_logros(lista_jugadores):
    """
    Obtiene el jugador con la mayor cantidad de logros en una lista de jugadores.

    Parámetros:
    - lista_jugadores (list): La lista de jugadores.

    Retorna:
    - dict: El diccionario del jugador con la mayor cantidad de logros.

    """
    return get_jugador_mas_longitud_clave(lista_jugadores, constantes.LOGROS)


def estadisticas_por_indice(jugadores, indice):
    """
    Imprime las estadísticas de un jugador específico en una lista de jugadores.

    Parámetros:
    - jugadores (list): La lista de jugadores.
    - indice (int): El índice del jugador en la lista.

    """
    jugador = jugadores[indice]
    nombre_jugador = jugador[constantes.NOMBRE]
    estadisticas = parsear_estadisticas(jugador[constantes.ESTADISTICAS])
    imprimir([nombre_jugador, estadisticas])

def obtener_cantidades_por_clave(clave, lista_jugadores):
    """
        Retorna un diccionario cuyas claves corresponden a los distintos valores de la clave, y el valor representa la cantidad de apariciones de dicho valor en la lista de jugadores

        Recibe:
        - clave: La clave sobre la cual buscar y agrupar.
        - lista_jugadores: La lista de jugadores.

        Retorna: El diccionario con las cantidades.
    """
    cantidades = {}
    for jugador in lista_jugadores:
        valor = jugador[clave]
        if valor not in cantidades:
            cantidades[valor] = 0
        cantidades[valor] += 1
    return cantidades

def obtener_jugadores_y_cantidad_Allstar(lista_jugadores):
    for jugador in lista_jugadores:
        cantidad_allstar = obtener_cantidad_veces_allstar(jugador)
        jugador[constantes.CLAVE_CANTIDAD_ALLSTAR] = cantidad_allstar
    return lista_jugadores

def obtener_cantidad_veces_allstar(jugador):
    logros = jugador[constantes.LOGROS]
    patron = r";([0-9]+) " + f"{constantes.VECES_ALL_STAR}"
    texto = ";".join(logros)
    ocurrencias = re.findall(patron, texto)
    if len(ocurrencias) > 0:
        return int(ocurrencias[0])
    return 0
        

def obtener_jugador_mas_temporadas_jugadas(lista_jugadores):
    """
    Obtiene el jugador con la mayor cantidad de temporadas jugadas en una lista de jugadores.

    Parámetros:
    - lista_jugadores (list): La lista de jugadores.

    Retorna:
    - dict: El diccionario del jugador con la mayor cantidad de temporadas jugadas.

    """
    return calcular_max_estadistica(constantes.TEMPORADAS, lista_jugadores)


def obtener_jugador_mayor_bloqueos_totales(lista_jugadores):
    """
    Obtiene el jugador con la mayor cantidad de bloqueos totales en una lista de jugadores.

    Parámetros:
    - lista_jugadores (list): La lista de jugadores.

    Retorna:
    - dict: El diccionario del jugador con la mayor cantidad de bloqueos totales.

    """
    return calcular_max_estadistica(constantes.BLOQUEOS_TOTALES, lista_jugadores)


def obtener_jugador_mayor_robos_totales(lista_jugadores):
    """
    Obtiene el jugador con la mayor cantidad de robos totales en una lista de jugadores.

    Parámetros:
    - lista_jugadores (list): La lista de jugadores.

    Retorna:
    - dict: El diccionario del jugador con la mayor cantidad de robos totales.

    """
    return calcular_max_estadistica(constantes.ROBOS_TOTALES, lista_jugadores)


def obtener_jugador_mayor_rebotes_totales(lista_jugadores):
    """
    Obtiene el jugador con la mayor cantidad de rebotes totales en una lista de jugadores.

    Parámetros:
    - lista_jugadores (list): La lista de jugadores.

    Retorna:
    - dict: El diccionario del jugador con la mayor cantidad de rebotes totales.

    """
    return calcular_max_estadistica(constantes.REBOTES_TOTALES, lista_jugadores)


def obtener_jugador_mayor_porcentaje_tiros_campo(lista_jugadores):
    """
    Obtiene el jugador con el mayor porcentaje de tiros de campo en una lista de jugadores.

    Parámetros:
    - lista_jugadores (list): La lista de jugadores.

    Retorna:
    - dict: El diccionario del jugador con el mayor porcentaje de tiros de campo.

    """
    return calcular_max_estadistica(constantes.PORCENTAJE_TIROS_DE_CAMPO, lista_jugadores)


def obtener_jugador_mayor_asistencias(lista_jugadores):
    """
    Obtiene el jugador con la mayor cantidad de asistencias totales en una lista de jugadores.

    Parámetros:
    - lista_jugadores (list): La lista de jugadores.

    Retorna:
    - dict: El diccionario del jugador con la mayor cantidad de asistencias totales.

    """
    return calcular_max_estadistica(constantes.ASISTENCIAS_TOTALES, lista_jugadores)


def obtener_jugadores_mas_puntos_partido_que_promedio(lista_jugadores, valor):
    """
    Obtiene los jugadores que tienen más puntos por partido que un valor específico en una lista de jugadores.

    Parámetros:
    - lista_jugadores (list): La lista de jugadores.
    - valor (float): El valor de referencia para comparar los puntos por partido.

    Retorna:
    - list: Una lista de diccionarios de los jugadores que tienen más puntos por partido que el valor especificado.

    """
    return obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, constantes.PROMEDIO_PUNTOS_POR_PARTIDO)


def obtener_jugadores_mas_que_valor_por_estadistica(lista_jugadores, valor, estadistica):
    """
    Obtiene los jugadores que tienen una estadística mayor que un valor específico en una lista de jugadores.

    Parámetros:
    - lista_jugadores (list): La lista de jugadores.
    - valor (float): El valor de referencia para comparar la estadística.
    - estadistica (str): La clave de la estadística a comparar.

    Retorna:
    - list: Una lista de diccionarios de los jugadores que tienen la estadística mayor que el valor especificado.

    """
    return obtener_jugadores_comparados_estadistica(lista_jugadores, valor, estadistica, True)


def obtener_jugadores_comparados_estadistica(lista_jugadores, valor, estadistica, mayor):
    """
    Obtiene los jugadores que tienen una estadística mayor o menor que un valor específico en una lista de jugadores.

    Parámetros:
    - lista_jugadores (list): La lista de jugadores.
    - valor (float): El valor de referencia para comparar la estadística.
    - estadistica (str): La clave de la estadística a comparar.
    - mayor (bool): Indica si se debe comparar la estadística como mayor o menor que el valor.

    Retorna:
    - list: Una lista de diccionarios de los jugadores que cumplen la condición de comparación.

    """
    jugadores_devolver = []
    for jugador in lista_jugadores:
        if (jugador[constantes.ESTADISTICAS][estadistica] >= valor) == mayor:
            jugadores_devolver.append(jugador)
    return jugadores_devolver


def obtener_jugadores_rankeados_por_estadisticas(lista_jugadores, lista_rankings):
    """
    Obtiene la lista de jugadores con sus rankings de estadísticas actualizados.

    Parámetros:
    - lista_jugadores (list): La lista de jugadores.
    - lista_rankings (list): La lista de estadísticas a clasificar.

    Retorna:
    - list: Una lista de diccionarios de los jugadores con sus rankings actualizados.

    """
    for estadistica in lista_rankings:
        lista_ordenada = ordenar_por_estadistica(lista_jugadores, estadistica, False)
        for i in range(len(lista_ordenada)):
            jugador = lista_ordenada[i]
            if not constantes.RANKINGS in jugador:
                jugador[constantes.RANKINGS] = {}
            jugador[constantes.RANKINGS][estadistica] = i + 1

    return lista_ordenada
