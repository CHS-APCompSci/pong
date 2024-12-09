# IMPORTS
import pygame
from pygame import sprite as sp

# CLASSES

class Things (sp.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10,100))
        pygame.draw.rect(self.image, "red",pygame.Rect(100,100,10,100),width=0)
        self.rect = self.image

    def update(self, *args, **kwargs):
        pass