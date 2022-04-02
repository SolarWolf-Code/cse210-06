# Game includes following concepts from CSE210
# Abstraction, Encapsulation, Inheritance, Maintainability
# Project completed by Bradley Strange and Shutong Bao


# import modules
import pygame
import sys
import random

# import classes
from player import Player
from missile import Missile
from star import Star
from enemy import Enemy
from color import Color
# import variable
from screen import screen

# Initialize game
pygame.init()
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()


# Create sounds
missile_sound = pygame.mixer.Sound("missile.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")

# Create font
font = pygame.font.SysFont("Century Gothic", 24)

# Create objects
player = Player()
missiles = [Missile(), Missile(), Missile()]
enemies = []
for _ in range(5):
    enemies.append(Enemy())
stars = []
for _ in range(30):
    stars.append(Star())

# Send function if missile ready


def fire_missile(offset_x, offset_y):
    # Is the missile ready
    for missile in missiles:
        if missile.state == "ready":

            missile.fire(offset_x, offset_y)
            missile_sound.play()
            break

# Main function


def main():
    while True:
        for event in pygame.event.get():
            # Quit game if user clicks close button
            if event.type == pygame.QUIT:
                sys.exit()

            # Keyboard events
            if event.type == pygame.KEYDOWN:
                # Move up
                if event.key == pygame.K_UP:
                    player.up()
                # Move down
                elif event.key == pygame.K_DOWN:
                    player.down()
                # Move left
                elif event.key == pygame.K_LEFT:
                    player.left()
                # Move right
                elif event.key == pygame.K_RIGHT:
                    player.right()
                # Fire missile
                elif event.key == pygame.K_SPACE:
                    # Send current player position for correct missile position
                    fire_missile(player.x, player.y)

        # Update objects
        player.move()

        for missile in missiles:
            missile.move()

        for star in stars:
            star.move()

        for enemy in enemies:
            enemy.move()

            # Check for collision for rocket and enemy
            for missile in missiles:
                if enemy.distance(missile) < 20:
                    explosion_sound.play()
                    enemy.health -= 4
                    if enemy.health <= 0:
                        enemy.x = random.randint(800, 900)
                        enemy.y = random.randint(0, 550)

                        player.kills += 1
                        if player.kills % 10 == 0:
                            # Spawn boss
                            enemy.surface = pygame.image.load(
                                'boss.png').convert()
                            enemy.max_health = 50
                            enemy.health = enemy.max_health
                            enemy.dy = random.randint(-5, 5)
                            enemy.type = "boss"
                        else:
                            # otherwise keep spawning normal enemies
                            enemy.type = "enemy"
                            enemy.dy = 0
                            enemy.surface = pygame.image.load(
                                'enemy.png').convert()
                            enemy.max_health = random.randint(5, 15)
                            enemy.health = enemy.max_health
                    else:
                        enemy.x += 20

                    # Reset missile
                    missile.dx = 0
                    missile.x = 0
                    missile.y = 1000
                    missile.state = "ready"

                    # Add to score
                    player.score += 10

            # Check for collision on player and enemy
            if enemy.distance(player) < 20:
                explosion_sound.play()

                player.health -= random.randint(5, 10)
                enemy.health -= random.randint(5, 10)
                enemy.x = random.randint(800, 900)
                enemy.y = random.randint(0, 550)

                # If health is 0, quit game and display "game over"
                if player.health <= 0:
                    print("Game over!")
                    pygame.quit()
                    exit()

        # Fill the background color
        screen.fill(Color(0, 0, 0).to_tuple())

        # Render stars
        for star in stars:
            star.render()

        # Render objects
        player.render()

        for missile in missiles:
            missile.render()

        for enemy in enemies:
            enemy.render()

        # Ammo counter
        ammo = 0
        for missile in missiles:
            if missile.state == "ready":
                ammo += 1

        for x in range(ammo):
            # Draw ammo count on screen
            screen.blit(missile.surface, (700 + 30 * x, 20))

        # Draw the score
        score_surface = font.render(
            f"Score: {player.score} Kills: {player.kills}", True, Color(255, 255, 255).to_tuple())
        screen.blit(score_surface, (380, 20))

        pygame.display.flip()

        clock.tick(30)


main()
