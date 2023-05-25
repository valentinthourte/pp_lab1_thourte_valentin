import re
def validar_nombre(nombre, nombre_completo = False):
    patron = r"^[a-zA-Z ]+$"
    if nombre_completo:
        patron = r"^[a-zA-Z]+ [a-zA-Z]+$"
    ocurrencias = re.findall(patron, nombre)
    if len(ocurrencias) == 0:
        nombre = input("Por favor, ingrese un nombre válido, conformado únicamente por letras y espacios: ")
        validar_nombre(nombre)

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

def validar_indice(indice, cantidad_jugadores):
    indice = str(int(indice) - 1)
    patron = r"^[0-9]+$"
    ocurrencias = re.findall(patron, indice)
    if len(ocurrencias) == 0 or int(ocurrencias[0]) >= cantidad_jugadores:
        indice = input(f"Ingrese un índice válido, numérico positivo menor o igual a {cantidad_jugadores}: ")
        return validar_indice(indice, cantidad_jugadores)
    else:
        return int(indice)
