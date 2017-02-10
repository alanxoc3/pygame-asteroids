import pygame as pg
import random

CAPTION = "4-Direction Movement with Animation"
SCREEN_SIZE = (500, 500)

BACKGROUND_COLOR = pg.Color("black")
COLOR_KEY = pg.Color("white")

DIRECT_DICT = {pg.K_LEFT  : (-1, 0),
         pg.K_RIGHT : ( 1, 0),
         pg.K_UP  : ( 0,-1),
         pg.K_DOWN  : ( 0, 1)}

WHITE   = (255, 255, 255)
DARKGREEN = (  0, 155,   0)
GREEN     = (  0, 255,   0)  
BLACK     = (  0,   0,   0)
BGCOLOR   = BLACK





def load_assets():
  global ASTEROID_SHEET
  global LABEL
  global FONT
  global QUOTE1
  global QUOTE2
  
 

  random.seed()
  
  QUOTES1 = ["You've had a long day at work.", "Don't feel so tense,", "You need to treat yourself more."]
  QUOTES2 = ["You need to relax", "you're safe here.", "Play our game."]
  num = random.randint(0, 2)
  
  
  FONT = pg.font.Font(None, 30)
  LABEL = FONT.render("Press Any Key To Continue", 1, (255,255,255))
  QUOTE1 = FONT.render(QUOTES1[num], 1, (255,255,255))
  QUOTE2 = FONT.render(QUOTES2[num], 1, (255,255,255))
  ASTEROID_SHEET = pg.image.load("assets/asteroids.png").convert_alpha()
