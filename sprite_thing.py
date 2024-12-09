# IMPORTS
import pygame
from pygame import sprite as sp

# CLASSES

class Things (sp.Sprite):

    def __init__(self):
        # run original sprite setup instructions
        super().__init__()
        # make a surface the right size for your sprite
        # as a rectangle - even if it ends up as a ball
        self.image = pygame.Surface([10,100])
        # draw the thing correctly, using rect if drawing a rectangle
        # and circle if drawing a circle
        pygame.draw.rect(self.image, "red",pygame.Rect(0,0,10,100))
        # put ths size of the image into rect
        self.rect = self.image.get_rect()
        # set the starting point (x,y) for the thing
        self.rect.x = 50
        self.rect.y = 50

    def update(self, *args, **kwargs):
        pass