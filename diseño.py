import pygame as pg

pg.init()






# Config ventana
ANCHO_VENTANA = 600
ALTO_VENTANA = 600
TAMAÑO_CELDA = 60
MARGEN = 30
# Colores
BLANCO = (255, 255, 255)
CELESTE = (174, 179, 245)
GRIS_CLARO = (220, 220, 220)
GRIS_OSCURO = (100, 100, 100)
NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)
ROJO = (200, 0, 0)
AZUL = (0, 100, 200)
AMARILLO = (255, 200, 0)





# Config fuente
fuente = pg.font.Font(None,36)

# Creacion de ventana
ventana = pg.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pg.display.set_caption("Sudoku")

def dibujar_tablero():
    """Dibuja el tablero del juego"""
    
    ventana.fill(BLANCO)
    
    # Dibuja el fondo de los cuadrados
    for i in range(3):
        for j in range(3):
            x = MARGEN + j * TAMAÑO_CELDA * 3
            y = MARGEN + i * TAMAÑO_CELDA * 3
            # Alternar color
            if (i + j) % 2 == 0:
                pg.draw.rect(ventana, GRIS_CLARO,(x, y, TAMAÑO_CELDA * 3, TAMAÑO_CELDA * 3))

    #Dibujar las lineas
    for i in range(10):
        pg.draw.line(ventana,GRIS_OSCURO, (MARGEN, MARGEN + i * TAMAÑO_CELDA), (MARGEN + 9 * TAMAÑO_CELDA, MARGEN + i * TAMAÑO_CELDA), 1)
        pg.draw.line(ventana, GRIS_OSCURO, (MARGEN + i * TAMAÑO_CELDA, MARGEN), (MARGEN + i * TAMAÑO_CELDA, MARGEN + 9 * TAMAÑO_CELDA), 1)
        
    for i in range(4):
        pg.draw.line(ventana, NEGRO, (MARGEN, MARGEN + i * TAMAÑO_CELDA * 3), (MARGEN + 9 * TAMAÑO_CELDA, MARGEN + i * TAMAÑO_CELDA * 3), 2)
        pg.draw.line(ventana, NEGRO, (MARGEN + i * TAMAÑO_CELDA * 3, MARGEN), (MARGEN + i * TAMAÑO_CELDA * 3, MARGEN + 9 * TAMAÑO_CELDA), 2)


def dibujar_pantalla_nick(texto_ingresado):
    """
    Dibuja la pantalla de ingreso de nick
    Args:
        texto_ingresado: String con el texto actualmente ingresado
    """
    ventana.fill(BLANCO)
    
    fuente_input = pg.font.Font(None, 40)
    fuente_inst = pg.font.Font(None, 24)
    
    # Título
    titulo = fuente.render("Ingrese su Nick:", True, NEGRO)
    rect_titulo = titulo.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2 - 80))
    ventana.blit(titulo, rect_titulo)
    
    # Campo de texto
    ancho_campo = 400
    alto_campo = 50
    x_campo = (ANCHO_VENTANA - ancho_campo) // 2
    y_campo = ALTO_VENTANA // 2 - 20
    
    pg.draw.rect(ventana, NEGRO, (x_campo - 2, y_campo - 2, ancho_campo + 4, alto_campo + 4), 2)
    pg.draw.rect(ventana, BLANCO, (x_campo, y_campo, ancho_campo, alto_campo))
    
    # Texto ingresado
    if texto_ingresado:
        texto_surface = fuente_input.render(texto_ingresado, True, NEGRO)
        ventana.blit(texto_surface, (x_campo + 10, y_campo + 10))
    else:
        texto_placeholder = fuente_input.render("Escriba aquí...", True, GRIS_OSCURO)
        ventana.blit(texto_placeholder, (x_campo + 10, y_campo + 10))
        
    # Instrucciones
    instrucciones = fuente_inst.render("Presione ENTER para continuar", True, GRIS_OSCURO)
    rect_inst = instrucciones.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 60))
    ventana.blit(instrucciones, rect_inst)

def generar_tablero(dificultad):
    """
    Genera un tablero de Sudoku dinamicamente con tres niveles de dificultad
    Args:
        dificultad: "facil", "medio" o "dificil"
    Returns:
        Tupla: (tablero, celdas_originales) donde tablero es 9x9 y celdas_originales es un set
    """
    from validaciones import generar_solucion_completa
    import random
    
    # Crear tablero vacío
    tablero = [[0 for columna in range(9)] for fila in range(9)]
    generar_solucion_completa(tablero)
    
    # Determinar cuántos números mantener por región según dificultad
    numeros_por_dificultad = {"facil": 5, "medio": 4, "dificil": 3}
    cantidad = numeros_por_dificultad.get(dificultad, 5)
    
    # Guardar las celdas originales
    celdas_originales = set()
    
    # Para cada región 3x3, mantener 'cantidad' números aleatorios
    for region_fila in range(3):
        for region_col in range(3):
            # Obtener todas las celdas de esta región
            celdas_region = []
            for fila in range(region_fila * 3, region_fila * 3 + 3):
                for col in range(region_col * 3, region_col * 3 + 3):
                    celdas_region.append((fila, col))
            
            # Seleccionar aleatoriamente 'cantidad' celdas para mantener
            celdas_a_mantener = random.sample(celdas_region, cantidad)
            celdas_originales.update(celdas_a_mantener)
    
    # Crear el tablero inicial (poner 0 en las celdas que no son originales)
    tablero_inicial = [[0 for columna in range(9)] for fila in range(9)]
    for fila, col in celdas_originales:
        tablero_inicial[fila][col] = tablero[fila][col]
    
    return tablero_inicial, celdas_originales


def crear_boton(texto, x, y, color):
    """
    Dibuja un botón fijo con texto centrado
    """
    # Medidas del botón
    
    ancho, alto = 200, 60
   
    
    rect = pg.Rect(x, y, ancho, alto)
    
    pg.draw.rect(ventana, color, rect)
    pg.draw.rect(ventana, NEGRO, rect, 2)
    
    texto_surface = fuente.render(texto, True, NEGRO)
    texto_rect = texto_surface.get_rect(center=rect.center)
    ventana.blit(texto_surface, texto_rect)
    
    return rect


def dibujar_menu_principal():
    """
    Dibuja el menu principal
    """

    x = (ANCHO_VENTANA - 220) // 2
    y = 200
    espacio = 75
    
    ventana.fill(CELESTE)
    
    boton_nivel = crear_boton("Seleccionar Dificultad",x, y, AMARILLO)
    boton_jugar = crear_boton("Jugar",x, y + espacio, VERDE)
    boton_puntajes = crear_boton("Ver Puntajes",x, y + espacio * 2, AZUL)
    boton_salir = crear_boton("Salir",x, y + espacio * 3, ROJO)
    return boton_nivel, boton_jugar, boton_puntajes, boton_salir


def dibujar_seleccion_dificultad():
    """
    Dibuja la ventana en la que se selecciona la dificultad
    """
    x = (ANCHO_VENTANA - 220) // 2
    y = 200
    espacio = 75
    
    ventana.fill(CELESTE)
    
    titulo = fuente.render("Seleccionar dificultad", True, NEGRO)
    ventana.blit(titulo, titulo.get_rect(center=(ANCHO_VENTANA // 2, 150)))
    
    boton_facil = crear_boton("Facil",x, y, VERDE)
    boton_medio = crear_boton("Medio",x, y + espacio, AMARILLO)
    boton_dificil = crear_boton("Dificil",x, y + espacio * 2, ROJO)
    boton_volver = crear_boton("Volver",x, y + espacio * 3, GRIS_OSCURO)
    return boton_facil, boton_dificil, boton_medio, boton_volver
    















