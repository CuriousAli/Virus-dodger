import pygame as pg
from random import randint
import sys


pg.init()


SIZE = 800, 600
n = randint(1,15)

def rand_color():
    return (randint(0,255),randint(0,255),randint(0,255))


class Man:
    def __init__(self, color, x, y, rad = randint(10,20)):
        x, y = randint(rad, 800 - rad), randint(rad, 600 - rad)
        color = rand_color()
        self.x = x
        self.y = y
        self.color = color
        self.rad = rad

    def draw(self, screen):
        pg.draw.circle(screen, self.rad, (self.x, self.y), self.rad)


TITLE = "Test circle"
screen = pg.display.set_mode(SIZE)
pg.display.set_caption(TITLE)

pg.display.flip()
clock = pg.time.Clock()


game = True

while game:


    for i in pg.event.get():
        if i.type == pg.quit():
            game = False



