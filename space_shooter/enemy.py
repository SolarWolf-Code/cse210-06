import random
import pygame
from screen import screen
from color import Color


class Enemy(Color):
    def __init__(self):
        # Initialize enemy
        self.x = 800
        # Pick random y pos to start
        self.y = random.randint(0, 550)
        # Pick random speed
        self.dx = random.randint(10, 50) / -10
        self.dy = 0
        self.surface = pygame.image.load('enemy.png')
        self.max_health = random.randint(5, 15)
        self.health = self.max_health
        self.type = "enemy"

    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy

        # Border check
        if self.x < -30:
            self.x = random.randint(800, 900)
            self.y = random.randint(0, 550)

        # Check for border collision
        if self.y < 0:
            self.y = 0
            self.dy *= -1

        elif self.y > 550:
            self.y = 550
            self.dy *= -1

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def render(self):
        screen.blit(self.surface, (int(self.x), int(self.y)))

        # Draw health meter
        pygame.draw.line(screen, Color(0, 255, 0).to_tuple(), (int(self.x), int(self.y)), (int(
            self.x + (30 * (self.health/self.max_health))), int(self.y)), 2)
