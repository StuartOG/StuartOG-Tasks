import pygame
import math
import random
# Initialize the game engine
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW = (255 , 255, 0)
PURPLE = (150, 0, 150)
PINK = (255,192,203)
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Otis's test:")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
x_val = 0
y_val = 200
x_offset = 3
y_offset = 3
pi= 3.141592652
counter = 0
screenfill = BLUE
randomint = random.randint(1,4)
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
   
    
    screen.fill(screenfill)
    
    
    #draw stuff here:

    y_val = y_val+ y_offset
    x_val = x_val + x_offset
    if y_val < 0:
        y_offset = y_offset*-1
    elif y_val > 495:
        y_offset = y_offset*-1
    elif x_val < 0:
        x_offset = x_offset*-1
    elif x_val > 695:
        x_offset = x_offset*-1
    #end if

    if y_val < 0:
        screenfill = BLUE
    elif y_val > 495:
        screenfill = PINK
    elif x_val < 0:
        screenfill = PURPLE
    elif x_val > 695:
        screenfill = GREEN




    pygame.draw.circle(screen, YELLOW, [x_val, y_val] , 20)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
#endwhile
pygame.quit()