import pygame as pg

# MISC
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = (400,400)
BACKGROUNDCOLOR = "dark gray"
FRAMERATE = 30

# PADDLE
PADDLESPEED = PADDLESPX, PADDLESPY = (0,12)
PADDLETHICK = 12
PADDLELENGTH = 80
PADDLEOFFSET = 10
PADDLECOLORLEFT = "red"
PADDLECOLORRIGHT = "blue"

# BALL
BALLSPEED = BALLSPX, BALLSPY = (8,8)
BALLDIAM = 12
BALLCOLOR = "red"






# BUTTONS
    # quit
x = 5
y = 5
width = 70
height =20
QUITRECT = pg.Rect(x,y,width,height)
    # new game
ny = 5
nwidth = 110
nx = SCREENWIDTH - nwidth
nheight = 20
NEWGAMERECT = pg.Rect(nx,ny,nwidth, nheight)
    # score
sy = 5
swidth = 100
sx = SCREENWIDTH/2 - swidth/2
sheight = 20
SCORERECT = pg.Rect(sx,sy,swidth,sheight)

