

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
            
def validar_celda_individual(tablero, fila, columna):
    """
    Valida el numero en la celda    
    Args:
        tablero: tablero de 9x9
        fila: fila de la celda
        columna: columna de la celda
    Returns:
        bool
    """
    numero = tablero[fila][columna]
    if numero == 0:
        return False
    
    # Guardar temporalmente el numero
    numero_temp = tablero[fila][columna]
    tablero[fila][columna] = 0
    
    # Verificar validez
    es_valido = verificar_validez(tablero, fila, columna, numero_temp)
    
    # Restaurar el número
    tablero[fila][columna] = numero_temp
    
    return es_valido

def verificar_zona_completa(tablero, region_fila, region_col):
    """
    Verifica si una zona 3x3 está completa y correcta    
    Args:
        tablero: tablero de 9x9
        region_fila: fila de la región (0-2)
        region_col: columna de la región (0-2)    
    Returns:
        bool:
    """
    numeros_vistos = set()
    inicio_fila = region_fila * 3
    inicio_col = region_col * 3
    
    for fila in range(inicio_fila, inicio_fila + 3):
        for columna in range(inicio_col, inicio_col + 3):
            numero = tablero[fila][columna]
            if numero == 0:
                return False
            
            # Verificar que el número sea válido en esa posición
            es_valido = validar_celda_individual(tablero, fila, columna)
            if es_valido == False:
                return False  
            
            if numero in numeros_vistos:
                return False
            
            numeros_vistos.add(numero)
    
    # Verificar que tenga todos los números del 1 al 9
    tiene_todos = len(numeros_vistos) == 9
    if tiene_todos:
        return True
    else:
        return False


def validar_tablero_completo(tablero):
    """
    Valida el tablero completo
    Args:
        tablero
    """
    numeros_incorrectos = []
    zonas_completas = []
    matriz_completa = True
    
    # Verificar cada celda
    for fila in range(9):
        for columna in range(9):
            numero = tablero[fila][columna]
            if numero != 0:
                es_valido = validar_celda_individual(tablero, fila, columna)
                if es_valido == False:
                    numeros_incorrectos.append((fila, columna))
            else:
                numeros_incorrectos.append((fila, columna))
    
    # Verificar zonas completas
    for region_fila in range(3):
        for region_col in range(3):
            zona_completa = verificar_zona_completa(tablero, region_fila, region_col)
            if zona_completa == True:
                zonas_completas.append((region_fila, region_col))
    
    # Verificar si el tablero completo está correcto
    #matriz_completa = validar_tablero_completo(tablero)
    
    return numeros_incorrectos, zonas_completas, matriz_completa


