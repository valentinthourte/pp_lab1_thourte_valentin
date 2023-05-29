import constantes

import constantes

def mostrar_jugador_es_de_salon_fama(nombre, lista_jugadores):
    """
    Verifica si un jugador es miembro del Salón de la Fama y muestra un mensaje correspondiente.

    Recibe:
    - nombre: El nombre del jugador a verificar.
    - lista_jugadores: Lista de diccionarios que representan a los jugadores.

    No devuelve ningún valor.
    """
    if es_jugador_salon_fama(nombre, lista_jugadores):
        texto = constantes.TEXTO_ES_SALON_FAMA
    else:
        texto = constantes.TEXTO_NO_ES_SALON_FAMA
    print(texto.format(nombre))

def es_jugador_salon_fama(nombre, lista_jugadores):
    """
    Verifica si un jugador es miembro del Salón de la Fama.

    Recibe:
    - nombre: El nombre del jugador a verificar.
    - lista_jugadores: Lista de diccionarios que representan a los jugadores.

    Devuelve:
    - Booleano que indica si el jugador es miembro del Salón de la Fama (True) o no (False).
    """
    jugadores = encontrar_jugadores_por_clave(lista_jugadores, constantes.NOMBRE, nombre)
    if len(jugadores) != 0:
        jugador = jugadores[0] # Si no viene vacía, tiene un único elemento, porque la validación previa checkea que se ingrese un nombre completo. 
                               # Solo traería más de 1 si hubiese varios jugadores con el mismo nombre
        return tiene_logro(jugador, constantes.LOGRO_SALON_FAMA)

def tiene_logro(jugador, logro):
    """
    Verifica si un jugador tiene un logro específico.

    Recibe:
    - jugador: Diccionario que representa al jugador.
    - logro: El logro a verificar.

    Devuelve:
    - Booleano que indica si el jugador tiene el logro (True) o no (False).
    """
    return logro in jugador[constantes.LOGROS]

def encontrar_jugadores_por_clave(lista_jugadores, clave, valor):
    """
    Encuentra jugadores en una lista por una clave y un valor específicos.

    Recibe:
    - lista_jugadores: Lista de diccionarios que representan a los jugadores.
    - clave: La clave por la cual se realizará la búsqueda.
    - valor: El valor a comparar con la clave.

    Devuelve:
    - Lista de jugadores que coinciden con la clave y el valor especificados.
    """
    jugadores_coincidencia = []
    for jugador in lista_jugadores:
        if jugador_coincide_por_clave(jugador, clave, valor):
            jugadores_coincidencia.append(jugador)

    return jugadores_coincidencia

def jugador_coincide_por_clave(jugador, clave, valor):
    """
    Encuentra un jugador por una clave y un valor específicos.

    Recibe:
    - jugador: Diccionario que representa al jugador.
    - clave: La clave por la cual se realizará la búsqueda.
    - valor: El valor a comparar con la clave.

    Devuelve:
    - Booleano que indica si el jugador coincide con la clave y el valor especificado (True) o no (False).
    """
    return jugador[clave].lower().startswith(valor.lower())

