from matplotlib.pyplot import get
import pygame
from color import Color
from screen import screen


class Player():
    def __init__(self):
        # Start player in middle-left of screen
        self.x = 100
        self.y = 1000
        self.dy = 0
        self.dx = 0
        self.surface = pygame.image.load('player.png').convert()
        self.score = 0
        self.max_health = 20
        self.health = self.max_health
        self.kills = 0

    def position(self):
        return(self.x, self.y)

    def up(self):
        self.dy = -6

    def down(self):
        self.dy = 6

    def left(self):
        self.dx = -6

    def right(self):
        self.dx = 6

    def move(self):
        self.y = self.y + self.dy
        self.x = self.x + self.dx

        # Check if player collides with screen edges
        if self.y < 0:
            self.y = 0
            self.dy = 0

        elif self.y > 550:
            self.y = 550
            self.dy = 0

        if self.x < 0:
            self.x = 0
            self.dx = 0

        elif self.x > 200:
            self.x = 200
            self.dx = 0

        #print(self.x, self.y)
        return(self.x, self.y)

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def render(self):
        screen.blit(self.surface, (int(self.x), int(self.y)))

        # Draw health meter
        pygame.draw.line(screen, Color(0, 255, 0).to_tuple(), (int(self.x), int(self.y)), (int(
            self.x + (40 * (self.health/self.max_health))), int(self.y)), 2)
