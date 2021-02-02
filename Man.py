import pygame as pg
from random import randint
import sys


SIZE = 800, 600
rad = randint(10,20)
x = randint(rad, 800 - rad)
y = randint(rad, 600 - rad)



TITLE = "Test circle"
screen = pg.display.set_mode(SIZE)
pg.display.set_caption(TITLE)


def rand_color():
    return (randint(0,255),randint(0,255),randint(0,255))


color = rand_color()
color2 = rand_color()



pg.display.flip()
clock = pg.time.Clock()


play = True
while play:


    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

        screen.fill(color2)

        pg.draw.circle(screen, color, (x, y), rad)
        pg.display.flip()

        pkgp = pg.key.get_pressed()
        u = pkgp[pg.K_UP]
        d = pkgp[pg.K_DOWN]
        l = pkgp[pg.K_LEFT]
        r = pkgp[pg.K_RIGHT]

        ''' Circle moves more smoothly if mouse is moving on game window/ Dunno why it happens'''

        if u == True and y >= 30:
            y -= 10
        elif d == True and y <= 570:
            y += 10
        elif l == True and x >= 30:
            x -= 10
        elif r == True and x <= 770:
            x += 10


        clock.tick(60)

