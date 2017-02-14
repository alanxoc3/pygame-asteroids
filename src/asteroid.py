import pygame as pg
import tools
import assets
import itertools

class Asteroid(object):
  """
  The Asteroid class
  """
  SIZE = (72, 72)
  SHEET_DIM = (5, 4)
  
  def __init__(self, pos, speed):
    self.speed = speed
    self.redraw = True # Forces redraw if needed.
    self.animate_timer = 0.0
    self.animate_fps = 7
    self.make_frames()
    self.image = self.frames[0][0]
    self.rect = self.image.get_rect(center=pos)
    self.explode = False
    self.angle = 0
    self.deadTimer = 40
    self.dead = False

  def make_frames(self):
    self.frames = tools.split_sheet(assets.ASTEROID_SHEET, Asteroid.SIZE, Asteroid.SHEET_DIM)

  def make_image(self, now):
    """
    Update the sprite's animation as needed.
    """
    elapsed = now-self.animate_timer > 1000.0/self.animate_fps
    if self.redraw or elapsed:
      self.animate_timer = now
    self.redraw = False

  def updateAngle(self):
    if not self.explode:
      self.angle += 2
    else:
      self.angle += 45

  def disappear(self):
    if self.deadTimer > 0:
      self.deadTimer -= 1
    else:
      self.dead = True

  def mouseCollision(self):
    # True if the left button is pressed.
    if pg.mouse.get_pressed()[0]:
      point = pg.mouse.get_pos()

      # Check if mouse point collides with rectangle.
      if self.rect.collidepoint(point):
        self.explode = True

  def update(self, now, screen_rect):
    """
    Updates our player appropriately every frame.
    """
    if self.dead:
      return

    self.updateAngle()

    if not self.explode:
      self.mouseCollision()
      self.rect.x += 1
    else:
      self.disappear()

  def draw(self, surface):
    """
    Draws the player to the target surface.
    """
    if self.dead:
      return

    drawnImage, drawnRect = tools.rot_center(self.image, self.rect, self.angle)
    # surface.blit(drawnImage, drawnRect)

    tools.blit_alpha(surface, drawnImage, drawnRect.topleft, 255)
