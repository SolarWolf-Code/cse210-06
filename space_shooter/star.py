import random
import pygame
from screen import screen


class Star():
    def __init__(self):
        # Create stars by randomizing x and y and speed
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 550)
        self.dx = random.randint(10, 50) / -30
        # Pick random png from yellow, red, and white
        images = ["yellow_star.png",
                  "red_star.png", "white_star.png"]
        self.surface = pygame.image.load(random.choice(images))

    def move(self):
        self.x = self.x + self.dx

        # Border check
        if self.x < 0:
            self.x = random.randint(800, 900)
            self.y = random.randint(0, 550)

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def render(self):
        screen.blit(self.surface, (int(self.x), int(self.y)))
