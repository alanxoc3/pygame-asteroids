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

    def update(self, now, screen_rect):
        """
        Updates our player appropriately every frame.
        """
        pass

    def draw(self, surface):
        """
        Draws the player to the target surface.
        """
        surface.blit(self.image, self.rect)
