import constantes

def mostrar_jugador_es_de_salon_fama(nombre, lista_jugadores):
    if es_jugador_salon_fama(nombre, lista_jugadores):
        texto = constantes.TEXTO_ES_SALON_FAMA
    else:
        texto = constantes.TEXTO_NO_ES_SALON_FAMA
    print(texto.format(nombre))

def es_jugador_salon_fama(nombre, lista_jugadores):
    jugadores = encontrar_jugadores_por_clave(lista_jugadores, "nombre", nombre)
    if len(jugadores) != 0:
        jugador = jugadores[0] # Si no viene vacía, tiene un único elemento, porque la validación previa checkea que se ingrese un nombre completo. 
                               # Solo traería más de 1 si hubiese varios jugadores con el mismo nombre
        return tiene_logro(jugador, constantes.LOGRO_SALON_FAMA)
    
def tiene_logro(jugador, logro):
    return logro in jugador["logros"]

def encontrar_jugadores_por_clave(lista_jugadores, clave, valor):
    jugadores_coincidencia = []
    for jugador in lista_jugadores:
        if encontrar_jugador_por_clave(jugador, clave, valor):
            jugadores_coincidencia.append(jugador)

    return jugadores_coincidencia

def encontrar_jugador_por_clave(jugador, clave, valor):
    return jugador[clave].lower().startswith(valor.lower())
