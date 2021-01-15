# libraries for game
import pygame
import math
from random import randint



FPS = 60
SCREEN_WIDHT, SCREEN_HEIGHT = 1000, 800
N = randint(5, 10)      #generate quantity exemplars of virus



class Spawn_point:

    def __init__(self, ):
        pass

    def escape(self, x, y):
        '''
        Define location of savezone on game area
        '''
        pass

    def virus(self, x, y):
        '''
        Randomly sets location for spawn "Virus" exemplar
        '''
        pass
    def dodger(self, x, y):
        '''
        Set start location for "Dodger"
        '''
        pass


class Virus:
    def __init__(self   ):
        pass
    def shape(self):
        '''
        Define size, color for every exemplar of virus
        '''
        pass

    def movement(self):
        '''
        Speed, moving direction of shape
        '''
        pass


class Dodger:
    def __init__(self    ):
        pass
    def appearance(self):
        '''
        Define size color of dodger
        '''
        pass
    def control(self):
        '''
        Technical realisation "Dodger" conrols from keyboard
        '''
        pass
    def contact(self):
        '''
        Check interaction with "Virus" and escape point
        '''
        pass






