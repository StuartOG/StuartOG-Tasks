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
size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Otis's Space Invaders")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
#classes
class Snow(pygame.sprite.Sprite):
    
    def __init__(self, size):
        super().__init__()

        self.size = size
        size = random.randrange(20, 25)
        self.image = pygame.Surface([size * 2, size * 2])
        pygame.draw.circle(self.image, BLACK, (size, size), size)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800)
        self.rect.y = 0
        self.speed = random.randrange(1, 2)


    def update(self):
        if self.rect.y > 500:
            self.rect.y = -self.size
        else:
            self.rect.y = self.rect.y + self.speed
        #end if

class Player(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length, initial_x):
        super().__init__()
        self.x_val2 = x_val2
        self.width = s_width
        self.height = s_length
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK), 
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = 465
    

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800

        

# end Class snow



# Global variables
x_val = 400

x_val2 = 350


size = random.randrange(1,2)

all_sprites = pygame.sprite.Group()

player_group = pygame.sprite.Group()

invader_group = pygame.sprite.Group()
number_of_enemies = 10
for _ in range(number_of_enemies):
    flake = Snow(size)
    invader_group.add(flake)
    all_sprites.add(flake)

for _ in range(1):
    player = Player(40, 30, x_val2)
    player_group.add(player)
    all_sprites.add(player)
# for i in range (0, number_of_flakes):
#     flake = Snow(size, size)
#     snow_group.add(flake)
# Next i

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
    all_sprites.update()
    # --- Drawing code should go here
 
    

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    invader_group.draw(screen)
    player_group.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)