# Game Ping-Pong with AI (Version 1) in Python

import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Initialize paddles and ball
player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)

# Initialize ball speed
ball_speed_x = 7
ball_speed_y = 7

# Initialize opponent AI speed
opponent_speed = 5

# Game state
playing = False

def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not playing:
                playing = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += 10
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= 10

    # AI opponent control
    if playing:
        if opponent_paddle.centery < ball.centery:
            opponent_paddle.y += opponent_speed
        elif opponent_paddle.centery > ball.centery:
            opponent_paddle.y -= opponent_speed

    # Game logic
    if playing:
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y = -ball_speed_y

        if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
            ball_speed_x = -ball_speed_x

        if ball.left <= 0 or ball.right >= WIDTH:
            playing = False
            ball.x = WIDTH // 2 - BALL_RADIUS // 2
            ball.y = HEIGHT // 2 - BALL_RADIUS // 2

    # Drawing
    draw_objects()

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

