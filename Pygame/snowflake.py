import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
SNOW_COLOR = (255, 255, 255)
NUM_SNOWFLAKES = 100

# Snowflake class
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.size = random.randint(1, 5)
        self.speed = random.randint(1, 5)

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = -self.size
            self.x = random.randint(0, WIDTH)

    def draw(self, screen):
        pygame.draw.circle(screen, SNOW_COLOR, (self.x, self.y), self.size)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snowfall")

# Create snowflakes
snowflakes = [Snowflake() for _ in range(NUM_SNOWFLAKES)]

# Clock to control frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    for snowflake in snowflakes:
        snowflake.move()
        snowflake.draw(screen)

    pygame.display.flip()
    clock.tick(30)  # Adjust frame rate as needed

# Quit Pygame
pygame.quit()
