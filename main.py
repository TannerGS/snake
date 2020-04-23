import pygame
from pygame.locals import *
import random

pygame.init()

GREEN = (0, 250, 0)
FOOD_LENGTH = 10

WIDTH, HEIGHT = 500, 500
        
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

        
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Snake
class Snake:
    """ This is a class for the snake functionality. """

    def __init__(self, x, y, vel, segments):
        """ The constructor for the Snake class. """

        self.x = x
        self.y = y
        self.vel = vel
        self.segments = segments

    def move_right(self):
        """Move snake right"""
        self.x = self.x + self.vel

    def move_left(self):
        """ Move snake left."""
        self.x = self.x - self.vel

    def move_up(self):
        """ Move snake up."""
        self.y = self.y - self.vel

    def move_down(self):
        """ Move snake down."""
        self.y = self.y + self.vel

# Food
class Food:
    """ This is a class for the Food Functionality."""

    def __init__(self, x, y):
        """ The constructor for the Food class. """

        self.x = x
        self.y = y

# Score

# App
    pygame.quit()
