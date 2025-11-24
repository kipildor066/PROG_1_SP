import pygame as pg
import os


def musica_fondo():
    """
    Reproduce la musica de fondo
    """

    
    cancion = "tema_fondo.mp3"
        

    pg.mixer.init()
    pg.mixer.music.load(cancion)
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.2)




