"""# libraries for game
import pygame
import math
from random import randint, choice



pygame.init()


#setup of window
SIZE = 1000, 800
TITLE = "Dodge the virus"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)



RED = (255, 0, 0)
GREEN = (52, 166, 36)
WHITE = (255, 255, 255)
D_BLUE = (18, 0, 91)

game = 0


class Escape:
    def __init__(self, coords = None, color = WHITE, rad = 20 ):
        self.coords = coords[1000, 400]
        self.color = color
        self.rad = rad

    def draw_escape(self, x, y):
        '''
        Define location of savezone on game area
        '''
        pygame.draw.circle(screen, self.color, self.coords, self.rad)


class Virus:
    def __init__(self, start_coord = None, rad = 15,color = RED):
        if start_coord == None:
            start_coord = [randint(200,970), randint(30, 770)]

        self.start_coord = start_coord
        self.rad = rad
        self.color = color

    def draw_virus(self):
        '''
        Draw virus
        '''
        pygame.draw.circle(screen, self.color, start_coord, self.rad)

    def move(self):
        pass


class MovingVirus(Virus):
    def __init__(self, start_coord = None, color = None, rad = 15, a = (-8, 8)):
        super.__init__(start_coord, rad, color)
        self.sx = choice(a)
        self.sy = choice(a)

    def move(self):
        '''
        choice direction depends on screen's borders
        '''
        if 24  < start_coord[0] < 976:
            start_coord[0] += self.sx
        else:
            start_coord[0] -= self.sx

        if 24 < start_coord[1] < 776:
            start_coord[1] += self.sy
        else:
            start_coord[1] -= self.sy


class Dodger:
    def __init__(self, man_x = 10, man_y = 400, color = GREEN, rad = 10):
        self.man_x = man_x
        self.man_y = man_y
        self.color = color
        self.rad = rad

    def draw_man(screen, self):
        '''
        draw man
        '''
        pygame.draw.circle(screen, self.color, (self.man_x, self.man_y), self.rad)

    def control(self):
        '''
        Technical realisation  conrols of "Dodger" from keyboard by pressing "arrows"
        '''

        pkgp = pygame.key.get_pressed()
        u = pkgp[pygame.K_UP]
        d = pkgp[pygame.K_DOWN]
        l = pkgp[pygame.K_LEFT]
        r = pkgp[pygame.K_RIGHT]

        if u == True and self.man_y >= 14:
            self.man_y -= 4
        elif d == True and self.man_y <=786:
            self.man_y += 4
        elif l == True and self.man_x >= 14:
            self.man_x -= 4
        elif r == True and self.man_x <= 986:
            self.man_x += 4


class Gameplay:
    def __init__(self, N = randint(8, 15), game = 0):
        self.N = N
        self.addvirus()
        self.game = game


    def addvirus(self):
        '''
        Add new elem of virus on game field
        '''
        for i in range(self.N):
            Virus.draw_virus(screen)



    def contact(self, man_x, man_y, start_coord, coords, game):
        '''
        Check interaction with "Virus" and escape point
        '''

        if abs(self.man_x - start_coord[0]) < 15 or abs(self.man_y - start_coord[1]) < 15:
            game = -1
        elif abs(self.man_x - coords[0]) < 20 or abs(self.man_y - coords[0]) < 20:
            game = 1


clock = pygame.time.Clock()


while game == 0:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()"""
