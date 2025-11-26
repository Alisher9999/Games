# Game Car (Version 1) in Python

import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Car settings
car_width = 50
car_height = 80
car_speed = 5

# Obstacle settings
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_spawn_rate = 25

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 36)

# Player
player_car = pygame.Rect(WIDTH // 2 - car_width // 2, HEIGHT - car_height - 20, car_width, car_height)

# Obstacles
obstacles = []

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def spawn_obstacle():
    obstacle = pygame.Rect(random.randint(0, WIDTH - obstacle_width), 0, obstacle_width, obstacle_height)
    obstacles.append(obstacle)

def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_car)

    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_car.left > 0:
        player_car.x -= car_speed
    if keys[pygame.K_RIGHT] and player_car.right < WIDTH:
        player_car.x += car_speed

    # Move obstacles
    obstacles = [obstacle.move(0, obstacle_speed) for obstacle in obstacles]

    # Spawn new obstacles
    if random.randint(1, obstacle_spawn_rate) == 1:
        spawn_obstacle()

    # Check for collisions
    for obstacle in obstacles:
        if player_car.colliderect(obstacle):
            draw_text("Game Over", WHITE, WIDTH // 2 - 100, HEIGHT // 2 - 18)
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()

    # Remove obstacles that are out of the screen
    obstacles = [obstacle for obstacle in obstacles if obstacle.top < HEIGHT]

    # Drawing
    draw_objects()

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)




