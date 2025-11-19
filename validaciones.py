import random

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
            

def generar_solucion_completa(tablero):
    """
    Llena el tablero completo con una solución valida del Sudoku
    """
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:

                numeros = list(range(1, 10))
                random.shuffle(numeros)
                
                for numero in numeros:
                    if verificar_validez(tablero, fila, columna, numero):
                        tablero[fila][columna] = numero
                        
                        if generar_solucion_completa(tablero):
                            return True
                        
                        tablero[fila][columna] = 0
                
                return False
    return True









