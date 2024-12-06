import pygame as pg
from pygame import sprite as sp

import constants as k

# COMMANDS

# MY SPRITE CLASSES

class Paddles (sp.Sprite):
    # needs to start in the center when created
    centery = k.SCREENHEIGHT / 2 - k.PADDLELENGTH / 2

    def __init__(self,side="left"):
        # do all the normal sprite stuff
        super().__init__()
        # Ball will interact with all members of the container
        sp.Sprite.__init__(self, self.containers)
        # create a surface to use for the image
        self.paddle = pg.Surface((k.PADDLETHICK, k.PADDLELENGTH), pg.SRCALPHA)
        # make a left or right paddle
        if side == "left" or side == "LEFT" or side == "Left":
            # specify the x pos of the paddle
            self.centerx = k.PADDLEOFFSET
            # specify the color
            self.color = k.PADDLECOLORLEFT
        else:
            self.centerx = k.SCREENWIDTH-k.PADDLETHICK-k.PADDLEOFFSET
            self.color = k.PADDLECOLORRIGHT
        # put the surface on the image,
        # fill the image with color
        # draw the image
        self.image = self.paddle
        self.image.fill(self.color)
        pg.draw.rect(self.image, self.color, (self.centerx, self.centery, k.PADDLETHICK, k.PADDLELENGTH), width=0)
        self.speed = self.x, self.y = k.PADDLESPEED
        # fill in the size and x,y coordinates for the image
        self.rect = self.image.get_rect()
        self.rect.x = self.centerx
        self.rect.y = self.centery

    # make the paddle move by itself
    def update(self, *args, **kwargs):
        # speed x=0, only moves in y
        self.rect = self.rect.move(self.speed)
        # keep the paddle in bounds
        if self.rect.top < 0 or self.rect.bottom > k.SCREENHEIGHT:
            # reverse the paddles motion
            self.y = -self.y
            self.speed = (self.x, self.y)