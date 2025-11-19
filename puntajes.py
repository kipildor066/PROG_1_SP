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
    
    try:
        with open(ARCHIVO_PUNTAJES, 'r', encoding='utf-8') as archivo:
            puntajes = json.load(archivo)
            # Ordenar por puntaje descendente
            puntajes.sort(key=lambda x: x.get('puntaje', 0), reverse=True)
            return puntajes
    except (json.JSONDecodeError, IOError):
        return []

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
    try:
        with open(ARCHIVO_PUNTAJES, 'w', encoding='utf-8') as archivo:
            json.dump(puntajes, archivo, ensure_ascii=False, indent=2)
    except IOError:
        print(f"Error al guardar el puntaje de {nick}")

def obtener_top_5():
    """
    Obtiene los 5 mejores puntajes
    Returns:
        Lista con máximo 5 diccionarios con 'nick' y 'puntaje'
    """
    puntajes = cargar_puntajes()
    return puntajes[:5]



