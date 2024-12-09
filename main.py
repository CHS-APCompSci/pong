import pygame as pg
import pygame_widgets as widgets
from pygame_widgets.button import Button
import pygame_widgets.button as mybutt
import constants as k

# INITIALIZE THINGS
pg.init()
my_screen = pg.display.set_mode(k.SCREENSIZE)
my_screen.fill(k.BACKGROUNDCOLOR)
clock = pg.time.Clock()
running = True

#Commands
def restart_game():
    pass

def my_quit():
    global running
    running = False
    
#Buttons
restart_button = Button(my_screen,10,10,70,20,text="Restart", onclick= restart_game)
my_quit = mybutt.Button (my_screen,10,10,70,20,text="Quit",
                         radius = 5, onClick = my_quit)




#LOOP
while running:
    # boilerplate code for closing the window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # redraw the background
    # which clears the screen
    my_screen.fill(k.BACKGROUNDCOLOR)
    widgets.update(event)
    # redraws all the stuff
    pg.display.update()
    # set the frame rate
    dt = clock.tick(k.FRAMERATE)

#QUIT
pg.quit()