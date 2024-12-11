import pygame as pg
from pygame import sprite as sp
import constants as k

# SPRITE CLASSES
class Paddles(sp.Sprite):
    def __init__(self):
        super().__init__()
        self.paddle = pg.Surface((10,100), pg.SRCALPHA)
        self.image = self.paddle
        self.color = k.BLUE
        pg.draw.rect(self.image, self.color, (10, 10, 10, 100), width=0)
        self.rect = self.image.get_rect()
        self.image.fill(self.color)
        self.rect.x = k.WIDTH - 50
        self.rect.y= k.HEIGHT // 2 - k.PADDLE_HEIGHT // 2

    def paddlemove(self,updown):
        if updown:
            myspeed=(0,k.PADDLE_SPEED)
        else:
            myspeed=(0,-k.PADDLE_SPEED)
        self.rect=self.rect.move(myspeed)
        self.rect = self.rect.clamp(pg.Rect(0,0,k.WIDTH, k.HEIGHT))