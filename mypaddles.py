import pygame as pg
from pygame import sprite as sp
from random import randint, random

import constants as k

# COMMANDS

# MY SPRITE CLASSES

class Paddles (sp.Sprite):
    # needs to start in the center when created
    centery = k.SCREENHEIGHT / 2 - k.PADDLELENGTH / 2

    def __init__(self,side="left"):
        super().__init__()
        # Ball will interact with all members of the container
        sp.Sprite.__init__(self, self.containers)
        # create a surface to use for the image
        self.paddle = pg.Surface((k.PADDLETHICK, k.PADDLELENGTH))  # , pg.SRCALPHA)
        if (side == "left" or side == "LEFT" or side == "Left"):
            self.centerx = k.PADDLEOFFSET
            self.color = k.PADDLECOLORLEFT
        else:
            self.centerx = k.SCREENWIDTH-k.PADDLETHICK-k.PADDLEOFFSET
            self.color = k.PADDLECOLORRIGHT
        self.image = self.paddle
        self.speed = self.x, self.y = k.PADDLESPEED
        self.rect = self.image.get_rect()
        self.rect.x = self.centerx
        self.rect.y = self.centery
        self.image.fill(self.color)
        pg.draw.rect(self.image,self.color, (self.centerx,self.centery,k.PADDLETHICK,k.PADDLELENGTH),width=0)

    def update(self, *args, **kwargs):
        self.rect = self.rect.move(self.speed)
        if self.rect.top < 0 or self.rect.bottom > k.SCREENHEIGHT:
            self.y = -self.y
            self.speed = (self.x, self.y)