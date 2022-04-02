import pygame
from screen import screen
from player import Player


class Missile(Player):
    def __init__(self):
        self.x = 0
        self.y = 1000
        self.dx = 0
        self.surface = pygame.image.load('missile.png').convert()
        self.state = "ready"

    def fire(self, offset_x, offset_y):
        self.state = "firing"
        self.x = offset_x + 25
        self.y = offset_y + 16
        self.dx = 10

    def move(self):
        if self.state == "firing":
            self.x = self.x + self.dx

        if self.x > 800:
            self.state = "ready"
            self.y = 1000

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def render(self):
        screen.blit(self.surface, (int(self.x), int(self.y)))
