import pygame as pg
import pygame.sprite
import pygame_widgets as widgets
import constants as k
import spriteclass as c

#initialize
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((k.WIDTH, k.HEIGHT))
pg.display.set_caption("pingy pongy")

#sprites
mypaddle=c.Paddles()
myspritegroup = pygame.sprite.Group()
myspritegroup.add(mypaddle)


# loop
running = True
while running:
    screen.fill(k.GREEN)

    # event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Sprite Motion
    keys = pg.key.get_pressed()

    if keys[pg.K_UP]:
        mypaddle.paddlemove(False)
    if keys[pg.K_DOWN]:
        mypaddle.paddlemove(True)


    myspritegroup.draw(screen)
    # Refresh
    pg.display.flip()

    # frame rate
    clock.tick(60)


running = True

# LOOP
while running:
    # boilerplate
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # redraw the background
    screen.fill(k.GREEN)

    # redraws all the stuff
    pg.display.update()
    # set the frame rate
    dt = clock.tick(k.FRAMERATE)

# QUIT
pg.quit()
