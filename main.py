import pygame as pg
import pygame_widgets as widgets

import sprite_thing
import constants as k

# INITIALIZE THINGS
pg.init()
my_screen = pg.display.set_mode(k.SCREENSIZE)
my_screen.fill(k.BACKGROUNDCOLOR)
clock = pg.time.Clock()

running = True

mything = sprite_thing.Things()

#LOOP
while running:
    # boilerplate code for closing the window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # redrwaw the background
    # which clears the screen
    my_screen.fill(k.BACKGROUNDCOLOR)
    mything.update()
    # redraws all the stuff
    pg.display.flip()
    # set the frame rate
    dt = clock.tick(k.FRAMERATE)

#QUIT
pg.quit()