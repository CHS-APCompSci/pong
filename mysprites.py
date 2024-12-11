import pygame
from pygame import sprite as sp
import constants as k

# CLASSES

# use your own names for this
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
        # put the size of the image into rect
        self.rect = self.image.get_rect()
        # set the starting point (x,y) for the thing
        self.rect.x = 50
        self.rect.y = 50

    def paddlemove(self,updown):
        if updown:
            myspeed = (0, k.paddlespeed)
        else:
            myspeed = (0, -k.paddlespeed)
        self.rect = self.rect.move(myspeed)
        self.rect = self.rect.clamp(pygame.Rect(0, 0, k.WIDTH, k.HEIGHT))



