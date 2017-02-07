#! /usr/bin/env python

"""
A Relaxing Asteroids game.
-Written by: Alan Morgan and Cameron Fife.
"""

import os
import sys
import itertools
import asteroid as asts

import pygame as pg

import assets

class App(object):
  """
  A class to manage our event, game loop, and overall program flow.
  """
  def __init__(self):
    """
    Get a reference to the display surface; set up required attributes;
    and create a Player instance.
    """
    self.screen = pg.display.get_surface()
    self.screen_rect = self.screen.get_rect()
    self.clock  = pg.time.Clock()
    self.fps = 60
    self.done = False
    self.keys = pg.key.get_pressed()
    self.asteroid = asts.Asteroid(self.screen_rect.center, 3)

  def event_loop(self):
    """
    Pass events on to the player.
    """
    for event in pg.event.get():
      if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
        self.done = True
      elif event.type in (pg.KEYUP, pg.KEYDOWN):
        self.keys = pg.key.get_pressed() 

  def display_fps(self):
    """
    Show the program's FPS in the window handle.
    """
    caption = "{} - FPS: {:.2f}".format(assets.CAPTION, self.clock.get_fps())
    pg.display.set_caption(caption)

  def update(self):
    """
    Update the player.
    The current time is passed for purposes of animation.
    """
    now = pg.time.get_ticks()
    self.asteroid.update(now, self.screen_rect)

  def render(self):
    """
    Perform all necessary drawing and update the screen.
    """
    self.screen.fill(assets.BACKGROUND_COLOR)
    self.asteroid.draw(self.screen)
    pg.display.update()
    
  def main_loop(self):
    """
    Our main game loop; I bet you'd never have guessed.
    """
    showStartScreen()
    while not self.done:
      self.event_loop()
      self.update()
      self.render()
      self.clock.tick(self.fps)
      self.display_fps()


def split_sheet(sheet, size, columns, rows):
  """
  Divide a loaded sprite sheet into subsurfaces.
  
  The argument size is the width and height of each frame (w,h)
  columns and rows are the integer number of cells horizontally and
  vertically.
  """
  subsurfaces = []
  for y in range(rows):
    row = []
    for x in range(columns): 
      rect = pg.Rect((x*size[0], y*size[1]), size)
      row.append(sheet.subsurface(rect))
    subsurfaces.append(row)
  return subsurfaces
  

  
def checkForKeyPress():			
	  keyUpEvents = pg.event.get(pg.KEYUP)		
	  if len(keyUpEvents) == 0:		
	    return None		
	  if keyUpEvents[0].key == pg.K_ESCAPE:		
	    terminate()		
	  return keyUpEvents[0].key
  
def showStartScreen():
   titleFont = pg.font.Font('freesansbold.ttf', 100)
   
   
   
   titleSurf1 = titleFont.render('Wormy!', True, assets.WHITE, assets.DARKGREEN)
   titleSurf2 = titleFont.render('Wormy!', True, assets.GREEN)

   
   
   degrees1 = 0
   degrees2 = 0
   while True:
    
     """
    
     DISPLAYSURF.fill(BGCOLOR)
     rotatedSurf1 = pg.transform.rotate(titleSurf1, degrees1)
     rotatedRect1 = rotatedSurf1.get_rect()
     rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
     DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

     rotatedSurf2 = pg.transform.rotate(titleSurf2, degrees2)
     rotatedRect2 = rotatedSurf2.get_rect()
     rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
     DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

     
     
     drawPressKeyMsg()
     """
     
     if checkForKeyPress():
       pg.event.get() # clear event queue
       return
     pg.display.update()
     """
     pg.FPSCLOCK.tick(FPS)
     """
     degrees1 += 3 # rotate by 3 degrees each frame
     degrees2 += 7 # rotate by 7 degrees each frame


def main():
  """
  Prepare our environment, create a display, and start the program.
  """
  os.environ['SDL_VIDEO_CENTERED'] = '1'
  pg.init()
  pg.display.set_caption(assets.CAPTION)
  pg.display.set_mode(assets.SCREEN_SIZE)

  assets.load_assets()

  App().main_loop()
  pg.quit()
  sys.exit()

if __name__ == "__main__":
  main()
