import pygame as pg
import pygame_widgets
from pygame_widgets.button import Button

import constants as k

# INITIALIZE THINGS
pg.init()
my_screen = pg.display.set_mode(k.SCREENSIZE)
my_screen.fill(k.BACKGROUNDCOLOR)
clock = pg.time.Clock()

running = True
left_score = 0
right_score = 0

# COMMANDS
def my_quit():
    global running
    running = False

def new_game():
    score_button.setText(text_score(0,1))

def score_click():
    score_button.setText(text_score(1,0))

def text_score(dleft=0, dright=0):
    global left_score, right_score
    left_score = left_score + dleft
    right_score = right_score + dright
    my_text = str(left_score) + " :: " + str(right_score)
    return my_text

# BUTTONS
my_quit_button = Button(my_screen, k.QUITRECT.x, k.QUITRECT.y, k.QUITRECT.width, k.QUITRECT.height,
            text = "Quit", radius = 5, hoverColour = "red", onClick = my_quit)
new_game_button = Button(my_screen,k.NEWGAMERECT.x,k.NEWGAMERECT.y,k.NEWGAMERECT.width,k.NEWGAMERECT.height,
            text = "New Game", radius = 5, onClick = new_game)
score_button = Button(my_screen,k.SCORERECT.x,k.SCORERECT.y,k.SCORERECT.width,k.SCORERECT.height,
            text = text_score(),radius=5, colour=k.BACKGROUNDCOLOR, hoverColour=k.BACKGROUNDCOLOR,
            pressedColour=k.BACKGROUNDCOLOR, onClick=score_click)

#LOOP
while running:
    # boilerplate code for closing the window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # redrwaw the background
    # which clears the screen
    my_screen.fill(k.BACKGROUNDCOLOR)

    # redraws all the stuff
    pygame_widgets.update(event)
    pg.display.update()
    # set the frame rate
    dt = clock.tick(k.FRAMERATE)

#QUIT
pg.quit()