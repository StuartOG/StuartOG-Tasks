import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Define paddles and ball
player_paddle = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 20, 100, 10)
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)

# Initialize ball direction
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

# Initialize player's score
score = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Move the player's paddle
    if keys[pygame.K_LEFT] and player_paddle.left > 0:
        player_paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and player_paddle.right < WIDTH:
        player_paddle.x += PADDLE_SPEED

    # Update ball position
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collisions with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx = -ball_dx

    # Ball collision with top wall
    if ball.top <= 0:
        ball_dy = -ball_dy

    # Ball collision with player's paddle
    if ball.colliderect(player_paddle) and ball_dy > 0:
        ball_dy = -ball_dy
        score += 1

    # Ball missed by player
    if ball.bottom >= HEIGHT:
        # Game over logic
        running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

    clock.tick(60)

# Game over screen
font = pygame.font.Font(None, 72)
text = font.render("Game Over", True, WHITE)
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(text, text_rect)
pygame.display.update()

# Wait for a few seconds before exiting
pygame.time.wait(3000)

# Quit Pygame
pygame.quit()
