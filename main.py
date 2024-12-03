import pygame as pg
import pygame_widgets as widgets
from spritecutter import imagecutter

import constants as k

# INITIALIZE THINGS
pg.init()
my_screen = pg.display.set_mode(k.SCREENSIZE)
my_screen.fill(k.BACKGROUNDCOLOR)
clock = pg.time.Clock()

trish = imagecutter("trish.png",500,500,1, 1)
trish.cut()

running = True

#LOOP
while running:
    # boilerplate code for closing the window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    keys = pg.key.get_pressed()
    # when D or A are pressed
    # set the direction of the hero
    direction = keys[pg.K_UP] - keys[pg.K_DOWN]

    # redrwaw the background
    # which clears the screen
    my_screen.fill(k.BACKGROUNDCOLOR)

    # redraws all the stuff
    pg.display.update()
    # set the frame rate
    dt = clock.tick(k.FRAMERATE)

#QUIT
pg.quit()