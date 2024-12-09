import pygame as pg
from pygame import sprite as sp
import constants as k

# SPRITE CLASSES
class Paddles(sp.Sprite):
    def __init__(self):
        super().__init__()
        self.paddle = pg.Surface((10,100), pg.SRCALPHA)
        self.image = self.paddle
        self.color = "red"
        pg.draw.rect(self.image, self.color, (10,15),(10,60), width=0)
        self.rect = self.image.get_rect()
        self.image.fill(self.color)



