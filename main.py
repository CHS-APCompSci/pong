import pygame as pg
import pygame_widgets as widgets
import constants as k
import spriteclass

#initialize
pg.init()
clock = pg.time.Clock()
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("pingy pongy")

#sprites
myrightpaddle = spriteclass.Paddles()
#myleftpaddle = Paddles("left")

# general paddle
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 15

# right paddle start pos
right_paddle_x = WIDTH - 50
right_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

# Color settings
BLUE = ("#3776ab")
GREEN = ("#50C878")

# Clock
clock = pg.time.Clock()

# loop
running = True
while running:
    screen.fill(GREEN)

    # event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Keys
    keys = pg.key.get_pressed()

    if keys[pg.K_UP] and right_paddle_y > 0:
        right_paddle_y -= PADDLE_SPEED
    if keys[pg.K_DOWN] and right_paddle_y < HEIGHT - PADDLE_HEIGHT:
        right_paddle_y += PADDLE_SPEED

    # draw
    pg.draw.rect(screen, BLUE, (right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    myrightpaddle.update()
    # Refresh
    pg.display.flip()

    # frame rate
    clock.tick(60)

# PADDLES
paddle_width, paddle_height = 20, 120
right_paddle_y = right_paddle_y = HEIGHT / 2 - paddle_height / 2
right_paddle_x, right_paddle_x = 100 - paddle_width / 2, WIDTH - (100 - paddle_width / 2)

running = True

# LOOP
while running:
    # boilerplate
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # redrwaw the background
    # which clears the screen
    SCREEN.fill(k.BACKGROUNDCOLOR)

    # redraws all the stuff
    pg.display.update()
    # set the frame rate
    dt = clock.tick(k.FRAMERATE)

# QUIT
pg.quit()
