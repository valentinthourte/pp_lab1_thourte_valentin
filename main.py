from Validaciones.validaciones import *
from Funciones.funciones_encontrar import *
from Funciones.funciones_mostrar import *
from Archivos.archivos import leer_archivo
from menu import *
import constantes

def main():
    lista_jugadores = leer_archivo("dt", "json")
    cantidad_jugadores = len(lista_jugadores)
    lista_rankings = [constantes.PUNTOS_TOTALES, constantes.REBOTES_TOTALES, constantes.ASISTENCIAS_TOTALES, constantes.ROBOS_TOTALES]
    continuar = True
    while continuar:
        opcion = pedir_opcion_hasta__que_sea_valida()
        match opcion:
            case 1:
                imprimir_nombre_y_posicion_jugadores(lista_jugadores)
            case 2:
                indice = pedir_indice(cantidad_jugadores)
                estadisticas_por_indice(lista_jugadores, indice)
            case 3:
                indice = pedir_indice(cantidad_jugadores)
                mostrar_estadisticas_y_guardar(lista_jugadores, indice)
            case 4:
                nombre = pedir_nombre(False)
                mostrar_logros_por_nombre(lista_jugadores, nombre)
            case 5:
                mostrar_promedio_puntos_por_partido_ascendente(lista_jugadores)
            case 6:
                nombre = pedir_nombre(True)
                mostrar_jugador_es_de_salon_fama(nombre, lista_jugadores)
            case 7:
                mostrar_jugador_mayor_rebotes_totales(lista_jugadores)
            case 8:
                mostrar_jugador_mayor_porcentaje_tiros_campo(lista_jugadores)
            case 9:
                mostrar_jugador_mayor_asistencias(lista_jugadores)
            case 10:
                valor = pedir_valor_para_promedio()
                mostrar_jugadores_promedian_mas_puntos_por_partido(lista_jugadores, valor)
            case 11:
                valor = pedir_valor_para_promedio()
                mostrar_jugadores_promedian_mas_rebotes_por_partido(lista_jugadores, valor)
            case 12:
                valor = pedir_valor_para_promedio()
                mostrar_jugadores_promedian_mas_asistencias_por_partido(lista_jugadores, valor)
            case 13:
                mostrar_jugador_mayor_robos_totales(lista_jugadores)
            case 14:
                mostrar_jugador_mayor_bloqueos_totales(lista_jugadores)
            case 15:
                valor = pedir_valor_para_promedio()
                mostrar_jugadores_promedian_mas_porcentaje_tiros_libres(lista_jugadores, valor)
            case 16:
                mostrar_promedio_puntos_por_partido_excluyendo_peor(lista_jugadores)
            case 17:
                mostrar_jugador_con_mas_logros(lista_jugadores)
            case 18:    
                valor = pedir_valor_para_promedio()
                mostrar_jugadores_promedian_mas_porcentaje_tiros_triples(lista_jugadores, valor)
            case 19:
                mostrar_jugador_mas_temporadas_jugadas(lista_jugadores)
            case 20:
                valor = pedir_valor_para_promedio()                
                mostrar_jugadores_promedian_mas_porcentaje_tiros_campo_por_posicion(lista_jugadores, valor)
            case 21:
                guardar_ranking_jugadores(lista_jugadores, lista_rankings)
            case 22:
                mostrar_cantidad_jugadores_por_posicion(lista_jugadores)
            case 23:
                mostrar_jugadores_ordenados_por_cantidad_AllStar(lista_jugadores)
            case 24:
                mostrar_jugador_mejor_estadistica_por_estadistica(lista_jugadores)
            case 25:
                mostrar_mejor_jugador_estadisticamente(lista_jugadores)
            case 0:
                continuar = False

        input("Presione enter para continuar.\n")

main()



