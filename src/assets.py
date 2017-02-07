import pygame as pg

CAPTION = "4-Direction Movement with Animation"
SCREEN_SIZE = (500, 500)

BACKGROUND_COLOR = pg.Color("black")
COLOR_KEY = pg.Color("white")

DIRECT_DICT = {pg.K_LEFT  : (-1, 0),
               pg.K_RIGHT : ( 1, 0),
               pg.K_UP    : ( 0,-1),
               pg.K_DOWN  : ( 0, 1)}

WHITE     = (255, 255, 255)
DARKGREEN = (  0, 155,   0)
GREEN     = (  0, 255,   0)  

def load_assets():
    global ASTEROID_SHEET
    ASTEROID_SHEET = pg.image.load("asteroids.png").convert_alpha()
