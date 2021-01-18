import pygame
import math
from random import randint


pygame.init()


#setup of window
SIZE = 800, 600
TITLE = "Test circle"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


def control():
    '''
    Technical realisation  conrols of "Dodger" from keyboard by pressing "arrows"
    '''

    pkgp = pygame.key.get_pressed()
    u = pkgp[pygame.K_UP]
    d = pkgp[pygame.K_DOWN]
    l = pkgp[pygame.K_LEFT]
    r = pkgp[pygame.K_RIGHT]

    if u == True and man_y >= 14:
        man_y -= 4
    elif d == True and self.man_y <= 786:
        man_y += 4
    elif l == True and man_x >= 14:
        man_x -= 4
    elif r == True and man_x <= 986:
        man_x += 4

def draw():
    pygame.draw.circle(screen, (60,255,255),(man_x, man_y), 10)






refresh_rate = 0

pygame.display.flip()
clock = pygame.time.Clock()


man_x = randint(100,700)
man_y = randint(100, 500)

draw()

while 1:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()

    clock.tick(10)
    pygame.display.update()
