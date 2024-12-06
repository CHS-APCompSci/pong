import pygame as pg
from pygame import sprite as sp
from random import randint, random

import spritecutter

import constants as k

# COMMANDS

# returns a random speed and direction for the ball
def randomspeed(a=5,b=3,A=k.BALLSPX,B=k.BALLSPY):
    x = randint(a,A)
    if random() < 0.5:
        x = -x
    y = randint(b,B)
    if random() < 0.5:
        y = -y
    return (x,y)


# MY SPRITE CLASSES

class Ball(sp.Sprite):
    # needs to start in the center when created
    centerx = k.SCREENWIDTH/2 - k.BALLDIAM/2
    centery = k.SCREENWIDTH/2 - k.BALLDIAM/2

    # create a surface to use for the image
    ball = pg.Surface((k.BALLDIAM,k.BALLDIAM), pg.SRCALPHA)

    def __init__(self):
        super().__init__()
        # Ball will interact with all members of the container
        sp.Sprite.__init__(self,self.containers)

        self.image = self.ball
        self.speed = self.x, self.y = randomspeed()
        self.diameter = k.BALLDIAM
        self.rect = self.image.get_rect()
        self.radius = k.BALLDIAM/2
        self.rect.x = self.centerx
        self.rect.y = self.centery
        self.image.fill(k.BALLCOLOR)
        pg.draw.circle(self.image,k.BALLCOLOR,(self.centerx,self.centery),self.radius)

    def update(self, *args, **kwargs):
        self.rect = self.rect.move(self.speed)
        if self.rect.top < 0 or self.rect.bottom > k.SCREENHEIGHT:
            self.y = -self.y
            self.speed = (self.x, self.y)
        # with no paddles
        if self.rect.left < 0 or self.rect.right > k.SCREENWIDTH:
            self.x = -self.x
            self.speed = (self.x, self.y)



