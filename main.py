import pygame as pg
import pygame_widgets as widgets

import constants as k
from mypaddles import Paddles

# INITIALIZE THINGS
pg.init()
my_screen = pg.display.set_mode(k.SCREENSIZE)
my_screen.fill(k.BACKGROUNDCOLOR)
clock = pg.time.Clock()

running = True

# ADD SPRITES TO GROUPS
paddlegroup = pg.sprite.RenderUpdates()
Paddles.containers = paddlegroup

# SPRITES
myrightpaddle = Paddles("right")
myleftpaddle = Paddles("left")

#LOOP
while running:
    # boilerplate code for closing the window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # redrwaw the background
    # which clears the screen
    my_screen.fill(k.BACKGROUNDCOLOR)

    paddlegroup.update()
    # redraws all the stuff
    dirty = paddlegroup.draw(my_screen)

    pg.display.update()
    # set the frame rate
    dt = clock.tick(k.FRAMERATE)

#QUIT
pg.quit()