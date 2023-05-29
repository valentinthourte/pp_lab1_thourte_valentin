import re
import re

def validar_nombre(nombre, nombre_completo=False):
    """
    Valida un nombre ingresado por el usuario.

    Recibe:
    - nombre: Nombre ingresado por el usuario como cadena de caracteres.
    - nombre_completo (opcional): Booleano que indica si se debe validar un nombre completo (nombre y apellido).

    Devuelve:
    - Nombre válido como cadena de caracteres o solicita nuevamente el ingreso al usuario.
    """
    patron = r"^[a-zA-Z ]+$"
    if nombre_completo:
        patron = r"^[a-zA-Z]+ [a-zA-Z]+$"
    ocurrencias = re.findall(patron, nombre)
    if len(ocurrencias) == 0:
        nombre = input("Por favor, ingrese un nombre válido, conformado únicamente por letras y espacios: ")
        return validar_nombre(nombre)
    else:
        return nombre

def validar_opcion(opcion, cantidad_opciones):
    """
        Valida que la opción ingresada por el usuario sea un valor válido, numerico positivo y que se encuentre dentro del rango de opciones
        
        Parametros: 
        opcion(str): La opcion ingresada por el usuario.
        cantidad_opciones(int): La cantidad de opciones del menú, para validar que la opcion ingresada este dentro del rango posible.

        Retorna:
        opcion(str): La opcion ingresada por el usuario. Si la opcion es invalida, retorna -1.
    """
    patron = r"^[0-9]{1,2}$"
    ocurrencias = re.findall(patron, opcion)
    if len(ocurrencias) == 0 or (int(ocurrencias[0]) > cantidad_opciones):
        return -1
    return opcion

import re

def validar_indice(indice, cantidad_jugadores):
    """
    Valida un índice ingresado por el usuario.

    Recibe:
    - indice: Índice ingresado por el usuario como cadena de caracteres.
    - cantidad_jugadores: Cantidad total de jugadores disponibles como entero.

    Devuelve:
    - Índice válido como entero o solicita nuevamente el ingreso al usuario.
    """
    indice = validar_indice_regex(indice)
    if indice != -1 and validar_indice_entero(indice, cantidad_jugadores) != -1:
        return indice
    else:
        indice = input(f"Ingrese un índice válido, numérico positivo menor o igual a {cantidad_jugadores}: ")
        return validar_indice(indice, cantidad_jugadores)

def validar_valor(valor):
    """
    Valida un valor ingresado por el usuario.

    Recibe:
    - valor: Valor ingresado por el usuario como cadena de caracteres.

    Devuelve:
    - Valor válido como número de punto flotante o solicita nuevamente el ingreso al usuario.
    """
    valor = validar_valor_regex(valor)
    if valor == -1:
        valor = input("Ingrese un valor válido, numérico mayor a 0: ")
        return validar_valor(valor)
    else:
        return valor

def validar_indice_regex(indice):
    """
    Valida un índice utilizando expresiones regulares.

    Recibe:
    - indice: Índice ingresado por el usuario como cadena de caracteres.

    Devuelve:
    - Índice válido como entero (restando 1 para ajustar a la indexación) o -1 si no es válido.
    """
    patron = r"^[1-9]+$"
    ocurrencias = re.findall(patron, indice)
    if len(ocurrencias) > 0:
        return int(indice) - 1
    else:
        return -1

def validar_valor_regex(valor):
    """
    Valida un valor utilizando expresiones regulares.

    Recibe:
    - valor: Valor ingresado por el usuario como cadena de caracteres.

    Devuelve:
    - Valor válido como número de punto flotante o -1 si no es válido.
    """
    patron = r"^[0-9.]+$"
    ocurrencias = re.findall(patron, valor)
    if len(ocurrencias) > 0:
        return float(valor)
    else:
        return -1

def validar_indice_entero(indice, cantidad_jugadores):
    """
    Valida un índice entero.

    Recibe:
    - indice: Índice ingresado por el usuario como entero.
    - cantidad_jugadores: Cantidad total de jugadores disponibles como entero.

    Devuelve:
    - Índice válido como entero o -1 si no es válido.
    """
    if indice < cantidad_jugadores:
        return indice
    else:
        return -1
