import re
def validar_nombre(nombre):
    patron = r"^[a-zA-Z ]+$"
    ocurrencias = re.findall(patron, nombre)
    if len(ocurrencias) == 0:
        nombre = input("Por favor, ingrese un nombre válido, conformado únicamente por letras y espacios: ")
        validar_nombre(nombre)