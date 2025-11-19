import pygame as pg
import sys
from diseño import *
from validaciones import *

def jugar(dificultad):
    from diseño import generar_tablero, dibujar_tablero
    
    tablero, celdas_originales = generar_tablero(dificultad)

    print(f"Iniciando juego en dificultad: {dificultad}.")

    
    numeros_generados = set()
    celda_seleccionada = None
    reloj = pg.time.Clock()
    ejecutando = True

    while ejecutando:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                print("Cerrando juego.")
                ejecutando = False
                
            elif evento.type == pg.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    celda_seleccionada = obtener_celda_desde_posicion(evento.pos)

            elif evento.type == pg.KEYDOWN:
                if celda_seleccionada and celda_seleccionada not in celdas_originales:
                    fila, columna = celda_seleccionada
                
                if evento.unicode.isdigit() and evento.unicode != '0':
                    tablero[fila][columna] = int(evento.unicode)
                    
                elif evento.key == pg.K_BACKSPACE or evento.key == pg.K_DELETE:
                    tablero[fila][columna] = 0
        
        

        

        dibujar_tablero()
        dibujar_numeros(tablero, celdas_originales,numeros_generados)
        pg.display.flip()
        reloj.tick(60)

    print("Juego finalizado")
    pg.quit()
    sys.exit()
    
def mostrar_menu_principal():
    """Muestra el menu de cuatro botones: "Dificultad", "jugar", "puntajes", "salir"
    """
    from diseño import dibujar_menu_principal
    
    reloj = pg.time.Clock()
    while True:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                return "Salir"
        
            elif evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                botones = dibujar_menu_principal()
                etiquetas = ["Dificultad", "Jugar", "Puntajes", "Salir"]
                for rect, accion in zip(botones, etiquetas):
                    if rect.collidepoint(evento.pos):
                        return accion
                
        dibujar_menu_principal()
        pg.display.flip()
        reloj.tick(60)
    
def mostrar_seleccion_dificultad():
    """
    Muestra el menu de seleccion de dificultad
    """ 
    from diseño import dibujar_seleccion_dificultad   
    reloj = pg.time.Clock()
    while True:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                return "Volver"
        
            elif evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                botones = dibujar_seleccion_dificultad()
                etiquetas = ["facil", "medio", "dificil", "volver"]
                for rect, accion in zip(botones, etiquetas):
                    if rect.collidepoint(evento.pos):
                        return accion
                
        dibujar_seleccion_dificultad()
        pg.display.flip()
        reloj.tick(60)
    
       
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
    
 
def dibujar_numeros(tablero, celdas_originales, numeros_generados):
    """
    Dibuja los números en el tablero
    Args:
        tablero = lugar donde va a dibujar
        celdas_originales = numeros por default que no se pueden modificar
    
    """
    
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] != 0:
                x = MARGEN + columna * TAMAÑO_CELDA + TAMAÑO_CELDA // 2
                y = MARGEN + fila * TAMAÑO_CELDA + TAMAÑO_CELDA // 2
                
                if (fila,columna) in numeros_generados:
                    color = NEGRO
                else:
                    color = GRIS_OSCURO
                
                texto = fuente.render(str(tablero[fila][columna]), True, color)
                rect_texto = texto.get_rect(center=(x, y))
                ventana.blit(texto, rect_texto)
 

def generar_solucion(tablero, numeros_generados):
    """
    Gestiona la solucion de el juego

    Args:
        tablero : tablero de 9x9
        numeros_generados: numeros generados para la solucion
    """
    celdas_vacias = set()
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                celdas_vacias.add((fila,columna))
                                
    generar_solucion_completa(tablero)
                    
    for fila in range(9):
        for columna in range(9):
            if (fila, columna) in celdas_vacias and tablero[fila][columna] != 0:
                numeros_generados.add((fila, columna))

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
        
        # Dibujar pantalla (lógica de dibujado en diseño.py)
        dibujar_pantalla_nick(texto_ingresado)
        pg.display.flip()
        reloj.tick(60)
    
    return texto_ingresado.strip() if texto_ingresado.strip() else "Jugador"
