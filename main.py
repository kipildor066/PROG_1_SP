import pygame as pg
import sys
from diseño import *
import os
from funciones import solicitar_nick, jugar, mostrar_menu_principal, mostrar_seleccion_dificultad
from puntajes import *


def main():
    """
    Punto de entrada del juego
    """
    reloj = pg.time.Clock()
    
    dificultad_actual = "medio"
    ejecutando = True
    
    while ejecutando:
        accion = mostrar_menu_principal()
        
        if accion == "Salir":
            ejecutando = False
        
        elif accion == "Dificultad":
            dificultad = mostrar_seleccion_dificultad()
            dificultad_actual = dificultad
            
        elif accion == "Jugar":
            nick = solicitar_nick()
            print(f"Jugador: {nick} | Dificultad: {dificultad_actual}")
            jugar(dificultad_actual)
            
        elif accion == "Puntajes":
            top_5 = obtener_top_5()
            print("Los puntajes mas altos son:")
            for i in range(len(top_5)):
                num = top_5[i]
                print(f"{i+1}.{top_5[i]['nick']} {top_5[i]['puntaje']}")
   
   
    pg.quit()
    sys.exit()

main()
