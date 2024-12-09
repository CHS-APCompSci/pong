import pygame as pg
import pygame.sprite
import pygame_widgets as widgets
import sprite_thing
import constants as k

pg.init()
my_screen = pg.display.set_mode(k.SCREENSIZE)
my_screen.fill(k.BACKGROUNDCOLOR)
clock = pg.time.Clock()
running = True

# MAKE THE SPRITE
mything = sprite_thing.Things()
# MAKE A SPRITE GROUP
myspritegroup = pygame.sprite.Group()
# ADD SPRITE TO SPRITE GROUP
myspritegroup.add(mything)




while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    my_screen.fill(k.BACKGROUNDCOLOR)

    # DRAW THE GROUP OF SPRITES
    myspritegroup.draw(my_screen)

    pg.display.update()
    dt = clock.tick(k.FRAMERATE)


pg.quit()