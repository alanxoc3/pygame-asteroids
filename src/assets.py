import pygame as pg

CAPTION = "4-Direction Movement with Animation"
SCREEN_SIZE = (500, 500)

BACKGROUND_COLOR = pg.Color("black")
COLOR_KEY = pg.Color("white")

DIRECT_DICT = {pg.K_LEFT  : (-1, 0),
               pg.K_RIGHT : ( 1, 0),
               pg.K_UP    : ( 0,-1),
               pg.K_DOWN  : ( 0, 1)}



def load_assets():
    global SKEL_IMAGE
    SKEL_IMAGE = pg.image.load("asteroids.png").convert_alpha()
