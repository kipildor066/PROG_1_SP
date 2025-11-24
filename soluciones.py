import random
from validaciones import *


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

