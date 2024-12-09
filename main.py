import pygame as pg
import pygame.sprite
import mysprites
import constants as k
import pygame_widgets as widgets


import constants as k
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((k.WIDTH, k.HEIGHT))
pg.display.set_caption("Pong Game")

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 6

# Left paddle initial position
left_paddle_x = 50
left_paddle_y = k.HEIGHT // 2 - PADDLE_HEIGHT // 2

# Color settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock for controlling frame rate
clock = pg.time.Clock()

mything = mysprites.Things()
# MAKE A SPRITE GROUP
# using your own names
myspritegroup = pygame.sprite.Group()
# ADD SPRITE TO SPRITE GROUP
myspritegroup.add(mything)

# Game loop
running = True
while running:
    screen.fill(BLACK)  # Fill the screen with black

    # Event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Key press handling for W (up) and S (down)
    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        mything.paddlemove(False)
    if keys[pg.K_s]:
        mything.paddlemove(True)

    # Draw the left paddle
    #pg.draw.rect(screen, WHITE, (left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    screen.fill(k.BACKGROUNDCOLOR)
    myspritegroup.draw(screen)
    # Refresh the screen
    pg.display.flip()

    # Set the frame rate (60 FPS)
    clock.tick(60)



#PADDLES
paddle_width, paddle_height= 20, 120
left_paddle_y= right_paddle_y= HEIGHT/2 -paddle_height/2
left_paddle_x, right_paddle_x=100-paddle_width/2, WIDTH -(100-paddle_width/2)




running = True



#LOOP
while running:
    # boilerplate code for closing the window
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

#QUIT
pg.quit()