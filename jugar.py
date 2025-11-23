import pygame as pg
import sys
from pantalla import *
from validaciones import *
from puntajes import *
from soluciones import *


        

def jugar(dificultad, nick):
    """
    Sudoku organizado segun dificultad elegida por el usuario

    Args:
        dificultad: facil, medio o dificil
        nick
    """
    from pantalla import generar_tablero, dibujar_tablero
    
    tablero, celdas_originales = generar_tablero(dificultad)

    print(f"Iniciando juego en dificultad: {dificultad}.")

    puntaje = 0
    zonas_completadas = set()
    numeros_generados = set()
    celda_seleccionada = None
    reloj = pg.time.Clock()
    ejecutando = True
    boton_validar_rect = None

    while ejecutando:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                print("Cerrando juego.")
                # Guardar el puntaje antes de salir
                guardar_puntaje(nick, puntaje)
                ejecutando = False
                
            elif evento.type == pg.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if boton_validar_rect.collidepoint(evento.pos):
                        # Validar el tablero completo
                        numeros_incorrectos, zonas_completas, matriz_completa = validar_tablero_completo(tablero)
                        
                        # Calcular nuevo puntaje
                        puntaje, zonas_completadas = calcular_puntaje(puntaje, numeros_incorrectos, zonas_completas, matriz_completa, zonas_completadas)
                    elif boton_reiniciar_rect.collidepoint(evento.pos):
                        jugar(dificultad, nick)
                    else:
                        celda_seleccionada = obtener_celda_desde_posicion(evento.pos)

            elif evento.type == pg.KEYDOWN:
                if evento.key == pg.K_g or evento.unicode.lower() == 'g':
                    generar_solucion_completa(tablero)
                elif celda_seleccionada and celda_seleccionada not in celdas_originales:
                    fila, columna = celda_seleccionada
                    if evento.unicode.isdigit() and evento.unicode != '0':
                        tablero[fila][columna] = int(evento.unicode)
                        
                    elif evento.key == pg.K_BACKSPACE or evento.key == pg.K_DELETE:
                        tablero[fila][columna] = 0
        
        

        

        dibujar_tablero()
        boton_validar_rect = crear_boton("Validar", 20, 605, GRIS_CLARO)
        boton_reiniciar_rect = crear_boton("Reiniciar", 385, 605, ROJO)
        dibujar_numeros(tablero, celdas_originales)
        dibujar_puntaje(puntaje)
        pg.display.flip()
        reloj.tick(60)

    print("Juego finalizado")
    pg.quit()
    sys.exit()
    

       
def obtener_celda_desde_posicion(pos):
    """
    Convierte posición del mouse (x, y) a coordenadas de celda (fila, columna)
    Args:
        pos = coordenada de x e y
    Return:
        interseccion entre fila y columna

    """
    x, y = pos
    if x < MARGEN or x > MARGEN + 9 * TAMAÑO_CELDA:
        return None
    if y < MARGEN or y > MARGEN + 9 * TAMAÑO_CELDA:
        return None
    
    columna = (x - MARGEN) // TAMAÑO_CELDA
    fila = (y - MARGEN) // TAMAÑO_CELDA
    
    return (fila, columna)
    
 

def solicitar_nick():
    """
    Solicita al usuario que ingrese su nick mediante un campo de texto
    
    Returns:
        String con el nick ingresado (máximo 20 caracteres)
    
    Nota: Necesita su propio loop porque pygame requiere capturar eventos
    continuamente para el input de texto y actualizar el cursor parpadeante.
    """
    texto_ingresado = ""
    activo = True
    reloj = pg.time.Clock()
    
    while activo:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                return "Jugador"
            
            elif evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RETURN or evento.key == pg.K_KP_ENTER:
                    if texto_ingresado.strip():
                        activo = False
                    else:
                        texto_ingresado = "Jugador"
                        activo = False
                elif evento.key == pg.K_BACKSPACE:
                    texto_ingresado = texto_ingresado[:-1]
                elif evento.key == pg.K_ESCAPE:
                    texto_ingresado = "Jugador"
                    activo = False
                elif len(texto_ingresado) < 20:
                    if evento.unicode.isprintable() and evento.unicode != '\r':
                        texto_ingresado += evento.unicode
        

        dibujar_pantalla_nick(texto_ingresado)
        pg.display.flip()
        reloj.tick(60)
    
    return texto_ingresado.strip() if texto_ingresado.strip() else "Jugador"



