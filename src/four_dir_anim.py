#! /usr/bin/env python

"""
This script implements a basic sprite that can only move orthogonally.
Orthogonal-only movement is slightly trickier than 8-direction movement
because you can't just create a simple movement vector.
Extra work must be done to make key overlaps execute cleanly.

-Written by Sean J. McKiernan 'Mekire'
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
        self.player = asts.Asteroid(self.screen_rect.center, 3)

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
        self.player.update(now, self.screen_rect)

    def render(self):
        """
        Perform all necessary drawing and update the screen.
        """
        self.screen.fill(assets.BACKGROUND_COLOR)
        self.player.draw(self.screen)
        pg.display.update()
        
    def main_loop(self):
        """
        Our main game loop; I bet you'd never have guessed.
        """
        while not self.done:
            self.event_loop()
            self.update()
            self.render()
            self.clock.tick(self.fps)
            self.display_fps()

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
