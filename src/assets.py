import pygame as pg
import random
import asteroid
import tools
from datetime import datetime

CAPTION = "4-Direction Movement with Animation"
SCREEN_SIZE = (500, 500)
HALF_SCREEN = (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2)

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

SIZE = (72, 72)
SHEET_DIM = (5, 4)

def load_assets():
  global ASTEROID_SHEET
  global LABEL
  global FONT
  global QUOTE1
  global QUOTE2
  global RELAX
  global DISPLAYSURF
  global SCREEN_RECT
  
  global score
  score = 0

  DISPLAYSURF = pg.display.set_mode(SCREEN_SIZE)
  SCREEN_RECT = pg.Rect( (0,0), SCREEN_SIZE )

  random.seed(datetime.now())
  
  RELAX = ["assets/relax1.wav", "assets/relax3.wav", "assets/relax2.wav"]
  QUOTES1 = ["You've must've had a long day at work.", "Don't feel so tense,", "You need to treat yourself more."]
  QUOTES2 = ["You need to relax", "you're safe here.", "Play our game."]

  num = random.randint(0, 2)
  
  FONT = pg.font.Font(None, 30)
  LABEL = FONT.render("Press Any Key To Continue", 1, (255,255,255))
  QUOTE1 = FONT.render(QUOTES1[num], 1, (255,255,255))
  QUOTE2 = FONT.render(QUOTES2[num], 1, (255,255,255))
  RELAX = pg.mixer.Sound(RELAX[num])
  ASTEROID_SHEET = pg.image.load("assets/asteroids.png")

  global FRAMES
  FRAMES = tools.split_sheet(ASTEROID_SHEET, SIZE, SHEET_DIM)
