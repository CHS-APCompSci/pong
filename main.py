import pygame as pg
import pygame_widgets as widgets

import constants as k
from mysprites import Ball

# INITIALIZE THINGS
pg.init()
my_screen = pg.display.set_mode(k.SCREENSIZE)
my_screen.fill(k.BACKGROUNDCOLOR)
clock = pg.time.Clock()
running = True

# ADD SPRITES TO GROUPS
ballgroup = pg.sprite.RenderUpdates()
Ball.containers = ballgroup

# SPRITES
myball = Ball()




#LOOP
while running:
    # boilerplate code for closing the window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # redrwaw the background
    # which clears the screen
    my_screen.fill(k.BACKGROUNDCOLOR)

    # update position of all sprites in ball group
    ballgroup.update()

    # redraws all the sprites in ballgroup
    dirty = ballgroup.draw(my_screen)
    # switches to the update display
    pg.display.update()
    # set the frame rate
    dt = clock.tick(k.FRAMERATE)

#QUIT
pg.quit()