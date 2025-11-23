

def verificar_validez(tablero, fila, columna, numero):
    """
    Verifica si un numero se puede colocar en determinada posicion

    Args:
        tablero: tablero de 9x9
        fila : fila del tablero
        columa : columna del tablero
        numero : numero a consultar
    """
    
    for i in range(9):
        if tablero[fila][i] == numero:
            return False
        
    for j in range(9):
        if tablero[j][columna] == numero:
            return False
        
    inicio_fila = (fila // 3) * 3
    inicio_col = (columna // 3) * 3
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_col, inicio_col + 3):
            if tablero[i][j] == numero:
                return False
    
    return True
            


def validar_tablero_completo(tablero):
    """
    Valida el tablero cuando el jugador presiona la tecla

    Args:
        tablero
    """

    numeros_incorrectos = []
    zonas_completas = []
    matriz_completa = True
    
    # verifica el numero en cada celda
    for fila in range(9):
        for columna in range(9):
            numero = tablero[fila][columna]
            if numero != 0:
                #guardamos el numero temporalmente
                numero_temp = tablero[fila][columna]
                #cambio el numero por 0 para validarlo
                tablero[fila][columna] = 0
                #verificar el numero
                if verificar_validez(tablero, fila, columna, numero_temp):
                    #si se valida, se restaura el numero_temp a su posicion
                    tablero[fila][columna] = numero_temp
                else:
                    numeros_incorrectos.append((fila,columna))
                    matriz_completa = False
                    tablero[fila][columna] = numero_temp
            elif numero == 0:
                numeros_incorrectos.append((fila,columna))
                


    #verificar zonas de 3x3
    for region_fila in range(3):
        for region_columna in range(3):
            for fila in range(region_fila * 3, region_fila * 3 + 3):   
                for columna in range(region_columna * 3, region_columna * 3 + 3):
                    numero = tablero[fila][columna]
                    numero_temp = tablero[fila][columna]
                    tablero[fila][columna] = 0
                    if verificar_validez(tablero, region_fila, region_columna, numero_temp):
                            #si se valida, se restaura el numero_temp a su posicion
                            tablero[fila][columna] = numero_temp
                            zonas_completas.append((region_fila,region_columna))
                    else:
                        matriz_completa = False
                        tablero[fila][columna] = numero_temp
            
    return numeros_incorrectos, zonas_completas, matriz_completa



