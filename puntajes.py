import json
import os

ARCHIVO_PUNTAJES = "puntajes.json"

def cargar_puntajes():
    """
    Carga los puntajes desde el archivo JSON
    Returns:
        Lista de diccionarios con 'nick' y 'puntaje', ordenados por puntaje descendente
    """
    if not os.path.exists(ARCHIVO_PUNTAJES):
        return []
    
    
    with open(ARCHIVO_PUNTAJES, 'r', encoding='utf-8') as archivo:
        puntajes = json.load(archivo)
        # Ordenar por puntaje descendente
        puntajes.sort(key=lambda x: x.get('puntaje', 0), reverse=True)
        return puntajes


def guardar_puntaje(nick, puntaje):
    """
    Guarda un nuevo puntaje en el archivo JSON
    Args:
        nick: Nombre del jugador
        puntaje: Puntaje obtenido
    """
    puntajes = cargar_puntajes()
    
    # Agregar nuevo puntaje
    puntajes.append({
        'nick': nick,
        'puntaje': puntaje
    })
    
    # Ordenar por puntaje descendente
    puntajes.sort(key=lambda x: x.get('puntaje', 0), reverse=True)
    
    # Guardar en archivo

    with open(ARCHIVO_PUNTAJES, 'w', encoding='utf-8') as archivo:
        json.dump(puntajes, archivo, ensure_ascii=False, indent=2)


def calcular_puntaje(puntaje_actual, numeros_incorrectos, zonas_completas, matriz_completa, zonas_completadas):
    """
    Calcula el puntaje segun lo validado

    Args:
        puntaje_actual: puntaje actual del jugador
        numeros_incorrectos (list): lista de (fila, columna) con números incorrectos
        zonas_completas (list): lista de tuplas (region_fila, region_col) de zonas completadas
        matriz_completa (bool): True si la matriz completa está correcta
        zonas_completadas: set de tuplas (region_fila, region_col) de zonas ya completadas anteriormente
        
    Returns:
        Tupla: (nuevo_puntaje, zonas_completadas_actualizado)
    """
    nuevo_puntaje = puntaje_actual
    
    # Descontar 1 punto por cada numero mal colocado
    nuevo_puntaje -= len(numeros_incorrectos)
    
    # Sumar 9 puntos por cada zona completada correctamente
    for zona in zonas_completas:
        if zona not in zonas_completadas:
            nuevo_puntaje += 9
            zonas_completadas.add(zona)
    
    # Sumar 81 puntos si la matriz completa está correcta
    if matriz_completa == True:
       
        print("¡Felicidades! Has completado el Sudoku.")
    
    return nuevo_puntaje, zonas_completadas


def obtener_top_5():
    """
    Obtiene los 5 mejores puntajes
    Returns:
        Lista con máximo 5 diccionarios con 'nick' y 'puntaje'
    """
    puntajes = cargar_puntajes()
    return puntajes[:5]



