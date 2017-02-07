import pygame as pg
import tools
import assets
import itertools

class Asteroid(object):
    """
    This class will represent our user controlled character.
    """
    SIZE = (72, 72)
    
    def __init__(self, pos, speed, facing=pg.K_RIGHT):
        """
        The pos argument is a tuple for the center of the player (x,y);
        speed is in pixels/frame; and facing is the Player's starting
        direction (given as a key-constant).
        """
        self.speed = speed
        self.direction = facing
        self.old_direction = None # Player's previous direction every frame.
        self.direction_stack = [] # Held keys in the order they were pressed.
        self.redraw = True # Forces redraw if needed.
        self.animate_timer = 0.0
        self.animate_fps = 7
        self.image = None
        self.walkframes = None
        self.walkframe_dict = self.make_frame_dict()
        self.adjust_images()
        self.rect = self.image.get_rect(center=pos)

    def make_frame_dict(self):
        """
        Create a dictionary of direction keys to frame cycles. We can use
        transform functions to reduce the size of the sprite sheet needed.
        """
        frames = tools.split_sheet(assets.SKEL_IMAGE, Asteroid.SIZE, 4, 1)[0]
        flips = [pg.transform.flip(frame, True, False) for frame in frames]
        walk_cycles = {pg.K_LEFT : itertools.cycle(frames[0:2]),
                       pg.K_RIGHT: itertools.cycle(flips[0:2]),
                       pg.K_DOWN : itertools.cycle([frames[3], flips[3]]),
                       pg.K_UP   : itertools.cycle([frames[2], flips[2]])}
        return walk_cycles

    def adjust_images(self, now=0):
        """
        Update the sprite's walkframes as the sprite's direction changes.
        """
        if self.direction != self.old_direction:
            self.walkframes = self.walkframe_dict[self.direction]
            self.old_direction = self.direction
            self.redraw = True
        self.make_image(now)

    def make_image(self, now):
        """
        Update the sprite's animation as needed.
        """
        elapsed = now-self.animate_timer > 1000.0/self.animate_fps
        if self.redraw or (self.direction_stack and elapsed):
            self.image = next(self.walkframes)
            self.animate_timer = now
        self.redraw = False

    def add_direction(self, key):
        """
        Add a pressed direction key on the direction stack.
        """
        if key in assets.DIRECT_DICT:
            if key in self.direction_stack:
                self.direction_stack.remove(key)
            self.direction_stack.append(key)
            self.direction = self.direction_stack[-1]

    def pop_direction(self, key):
        """
        Pop a released key from the direction stack.
        """
        if key in assets.DIRECT_DICT:
            if key in self.direction_stack:
                self.direction_stack.remove(key)
            if self.direction_stack:
                self.direction = self.direction_stack[-1]

    def get_event(self, event):
        """
        Handle events pertaining to player control.
        """
        if event.type == pg.KEYDOWN:
            self.add_direction(event.key)
        elif event.type == pg.KEYUP:
            self.pop_direction(event.key)

    def update(self, now, screen_rect):
        """
        Updates our player appropriately every frame.
        """
        self.adjust_images(now)
        if self.direction_stack:
            direction_vector = assets.DIRECT_DICT[self.direction]
            self.rect.x += self.speed*direction_vector[0]
            self.rect.y += self.speed*direction_vector[1]
            self.rect.clamp_ip(screen_rect)

    def draw(self, surface):
        """
        Draws the player to the target surface.
        """
        surface.blit(self.image, self.rect)
	
