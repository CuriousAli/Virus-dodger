# libraries for game
import pygame
import math
import random


FPS = 60
SCREEN_WIDHT, SCREEN_HEIGHT = 1000, 800


class Virus:
    def shape(self):
    '''Define size, color for every exemplar of virus'''

    def movement(self):
    '''Speed, moving direction of shape'''

    def contact(self):
    '''Check interaction with "Dodger" '''

    pass


class Dodger:
    def appearance(self):
    '''Define size color of dodger'''

    def control(self):
    '''Technical realisation "Dodger" conrols from keyboard'''

    pass


class Spawn_points:
    def escape_point_location(self, x,y):
    '''Spawn location of escape point on opposite part of game table'''

    def virus_spawnpoint(self):
    '''Randomly sets location for spawn "Virus" exemplar'''
    pass


