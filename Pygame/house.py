# Import a library of functions called 'pygame'
import pygame
import math

# Initialize the game engine
pygame.init()
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = (   255, 255, 0)
LIGHTBLUE = ( 0,  100, 200)

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Otis's Cool Game")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
#Global variables
x_val = 50
y_val = 24/6125 * x_val**2 + -2.798*x_val + 500
radius = 25
x_offset = 3
y_offset = math.sin(-2*x_val)
pi = 3.141592652
counter = 1
SUNCOLOUR = YELLOW
screenfill = LIGHTBLUE



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
    if x_val >= 0:
        x_val = x_val + x_offset
    if x_val > 350:
        y_val = y_val + y_offset
    else:
        y_val = y_val + -1*y_offset
    if x_val == 750:
        x_val = 0
        y_val = 175
        counter += 1
    if counter%2 == 0:
        SUNCOLOUR = BLACK
    else:
        SUNCOLOUR = YELLOW

    if counter%2 == 0:
        screenfill = BLACK
    else:
        screenfill = LIGHTBLUE
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(screenfill)

    pygame.draw.rect(screen, GREEN, [0, 300, 900, 300])
    pygame.draw.arc(screen, YELLOW, [-50, 100, 900, 300], 2*pi, pi, 5)
    pygame.draw.arc(screen, RED, [-50, 95, 900, 300], 2*pi, pi, 5)
    pygame.draw.arc(screen, GREEN, [-50, 105, 900, 300], 2*pi, pi, 5)
    pygame.draw.arc(screen, BLUE, [-50, 110, 900, 300], 2*pi, pi, 5)
    pygame.draw.circle(screen, SUNCOLOUR, [x_val, y_val], radius)
    pygame.draw.rect(screen, RED, [160, 150, 400, 250])
    pygame.draw.rect(screen, WHITE, [190, 180, 60, 50])
    pygame.draw.rect(screen, WHITE, [450, 180, 60, 50])
    pygame.draw.rect(screen, WHITE, [450, 300, 60, 50])
    pygame.draw.rect(screen, WHITE, [190, 300, 60, 50])
    pygame.draw.rect(screen, WHITE, [320, 300, 60, 100])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

