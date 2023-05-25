from Parcial1 import *
from Validaciones.validaciones_texto import *

def main():
    lista_jugadores = leer_archivo("dt", "json")
    cantidad_jugadores = len(lista_jugadores)
    continuar = True
    while continuar:
        opcion = pedir_opcion_hasta__que_sea_valida()
        match opcion:
            case 1:
                imprimir_jugadores(lista_jugadores)
            case 2:
                indice = input("Ingrese un índice.")
                indice = validar_indice(indice)
                estadisticas_por_indice(lista_jugadores, indice)
            case 3:
                indice = input("Ingrese un índice.")
                indice = validar_indice(indice, cantidad_jugadores)
                mostrar_estadisticas_y_guardar(lista_jugadores, indice)
            case 4:
                nombre = input("Ingrese un nombre: ")
                validar_nombre(nombre)
                mostrar_logros_por_nombre(lista_jugadores, nombre)
            case 5:
                imprimir_promedio_y_estadistica("promedio_puntos_por_partido", lista_jugadores)
                
            case 6:
                pass

            case 7:
                pass

            case 8:
                pass

            case 9:
                pass

            case 10:
                pass

            case 11:
                pass

            case 12:
                pass

            case 13:
                pass

            case 14:
                pass

            case 15:
                pass

            case 16:
                pass

            case 17:
                pass

            case 18:
                pass

            case 19:
                pass

            case 20:
                pass
            case 0:
                continuar = False
        input("Presione enter para continuar.")

main()

