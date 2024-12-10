import pygame as pg
import pygame.sprite
import pygame_widgets as widgets
import constants as k
import spriteclass

#initialize
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((k.WIDTH, k.HEIGHT))
pg.display.set_caption("pingy pongy")

#sprites
myrightpaddle = spriteclass.Paddles()
#myleftpaddle = Paddles("left")
spritesgroup = pygame.sprite.Group()
spritesgroup.add(myrightpaddle)


# general paddle
#PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
#PADDLE_SPEED = 15

# right paddle start pos
#right_paddle_x = WIDTH - 50
#right_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

# Color settings
#BLUE = ("#3776ab")
#GREEN = ("#50C878")

# Clock
clock = pg.time.Clock()

# loop
running = True
while running:
    screen.fill(k.GREEN)

    # event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Keys
    keys = pg.key.get_pressed()

    if keys[pg.K_UP] and k.right_paddle_y > 0:
        k.right_paddle_y -= k.PADDLE_SPEED
    if keys[pg.K_DOWN] and k.right_paddle_y < k.HEIGHT - k.PADDLE_HEIGHT:
        k.right_paddle_y += k.PADDLE_SPEED

    # draw
    #pg.draw.rect(screen, BLUE, (right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    spritesgroup.draw(screen)
    # Refresh
    pg.display.flip()

    # frame rate
    clock.tick(60)

# PADDLES
#paddle_width, paddle_height = 20, 120
#right_paddle_y = HEIGHT / 2 - paddle_height / 2
#right_paddle_x = 100 - paddle_width / 2, WIDTH - (100 - paddle_width / 2)

running = True

# LOOP
while running:
    # boilerplate
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # redraw the background
    # which clears the screen
    screen.fill(k.BACKGROUNDCOLOR)

    # redraws all the stuff
    pg.display.update()
    # set the frame rate
    dt = clock.tick(k.FRAMERATE)

# QUIT
pg.quit()
