import pygame
import math
import random
import os
import time
# Initialize the game engine
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = (255 , 255,   0)
PURPLE   = ( 150,   0, 150)
PINK     = ( 255, 192, 203)
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
rust = ((210,150,75))
dandilion_yellow = ((255,200,0))
highlighter = ((255,255,100))
sky_blue = ((0,255,255))
light_gray = ((200,200,200))
dark_gray = ((50,50,50))
tan = ((230,220,170))
coffee_brown =((200,190,140))
moon_glow = ((235,245,255))
nighttime = (19,24,98)
colours = [GREEN,RED,BLUE,PURPLE,PINK, blue_green, marroon, lime,gray,magenta,brown,forest_green,navy_blue,rust,dandilion_yellow,highlighter
           ,sky_blue,light_gray,dark_gray,tan,coffee_brown,moon_glow,nighttime]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Otis's pong game")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
#classes
class Snow(pygame.sprite.Sprite):
    
    #Constructor function
    def __init__(self, s_width, s_length):
        super().__init__()
        
        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(WHITE)
        self.speed = random.randrange(1,5)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(0,700)
        self.rect.y=random.randrange(0,400)

    #end of constructor function

    def update(self):
        if self.rect.y > 500:
            self.rect.y = -50
        else:
            self.rect.y = self.rect.y + self.speed

# end Class snow



# Global variables

size = random.randrange(2,6)

snow_group = pygame.sprite.Group()
number_of_flakes = 500
for i in range (0, number_of_flakes):
    flake = Snow(size, size)
    snow_group.add(flake)
# Next i

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
    snow_group.update()

    # --- Drawing code should go here
 
    

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(nighttime)
 
    snow_group.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)