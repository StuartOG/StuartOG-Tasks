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
colours = [GREEN,RED,BLUE,PURPLE,PINK, blue_green, marroon, lime,gray,magenta,brown,forest_green,navy_blue,rust,dandilion_yellow,highlighter
           ,sky_blue,light_gray,dark_gray,tan,coffee_brown,moon_glow]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Otis's pong game")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#classes
class Snow(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()

        self.size = size
        size = random.randrange(2, 6)
        self.image = pygame.Surface([size * 2, size * 2], pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (size, size), size)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800)
        self.rect.y = random.randrange(0, 400)
        self.speed = random.randrange(1, 5)
        self.horizontalspeed = random.randrange(-2,2)

    def update(self):
        if self.rect.y > 500:
            self.rect.y = -self.size
            self.rect.x = self.rect.x + self.horizontalspeed
        else:
            self.rect.y = self.rect.y + self.speed
        #end if
        if self.rect.y > 0:
            self.rect.x = self.rect.x + self.horizontalspeed
        if self.rect.x < 0 and self.rect.y > 500:
            self.rect.x = random.randrange(0,800)
        elif self.rect.x > 800 and self.rect.y > 500:
            self.rect.x = random.randrange(0,800)

#Global Variables
size = random.randrange(1,2)

snow_group = pygame.sprite.Group()
number_of_flakes = 50
for _ in range(number_of_flakes):
    flake = Snow(size)
    snow_group.add(flake)
# for i in range (0, number_of_flakes):
#     flake = Snow(size, size)
#     snow_group.add(flake)
# Next i

x_val = 350
y_val = 250
x_offset = 5
y_offset = 5
pi= 3.141592652
counter = 0
screenfill_fill = BLUE
randomint = random.randint(1,4)
y_val_2 = 200
x_val_2 = 5
y_val_3 = 200
lives = 5
text_font = pygame.font.SysFont(None, 30)
font = pygame.font.SysFont(None, 50)
end = ""
right_lives = 0
left_lives = 0


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
   
    
    screen.fill(screenfill_fill)
    
    
    snow_group.draw(screen)
    #draw stuff here:
    endmessage = font.render(end, True, BLACK)
    screen.blit(endmessage, [270,100])
    player_two_lifecount=font.render(str(left_lives), True, BLACK)
    screen.blit(player_two_lifecount, [100, 100])
    player_one_lifecount=font.render(str(right_lives), True, BLACK)
    screen.blit(player_one_lifecount, [600, 100])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y_val_2 -= 5
    if keys[pygame.K_s]:
        y_val_2 += 5

    if keys[pygame.K_UP]:
        y_val_3 -= 5
    if keys[pygame.K_DOWN]:
        y_val_3 += 5


    y_val = y_val+ y_offset
    x_val = x_val + x_offset

    if y_val < 0:
        y_offset = y_offset*-1 

    elif y_val > 495:
        y_offset = y_offset*-1 
        
    
    elif x_val < 20 and y_val >= y_val_2 and y_val <= y_val_2 + 100:
        x_offset = x_offset*-1 
        screenfill_fill=random.choice(colours)

    elif x_val > 665 and y_val >= y_val_3 and y_val <= y_val_3 + 100:
        x_offset = x_offset*-1 
        screenfill_fill=random.choice(colours)
        
    if x_val < 0 and y_val >= y_val_2+100:
        screenfill = RED
        x_val = 350
        y_val = 250
        screenfill = BLUE
        right_lives+= 1
    
    elif x_val < 0 and y_val <= y_val_2:
        screenfill = RED
        x_val = 350
        y_val = 250
        screenfill = BLUE
        right_lives += 1 
    
    if x_val > 700 and y_val >= y_val_3+100:
        screenfill = RED
        x_val = 350
        y_val = 250
        screenfill = BLUE
        left_lives += 1

    elif x_val > 700 and y_val <= y_val_3:
        screenfill = RED
        x_val = 350
        y_val = 250
        screenfill = BLUE
        left_lives += 1    
       
    
    if left_lives > 5:
        end = "Player One Wins"
        endmessage = font.render(end, True, BLACK)
        screen.blit(endmessage, [225,75])
        pygame.display.flip()
        time.sleep(1)
        done = True
    
    if right_lives > 5:
        end = "Player Two Wins"
        endmessage = font.render(end, True, BLACK)
        screen.blit(endmessage, [225,75])
        pygame.display.flip()
        time.sleep(1)
        done = True
    

    #end if
    pygame.draw.rect(screen, BLACK, (x_val, y_val, 12, 12))

    pygame.draw.rect(screen, YELLOW, (x_val, y_val , 10, 10))

    pygame.draw.rect(screen, BLACK, (5, y_val_2, 15, 100))

    pygame.draw.rect(screen, BLACK, (680, y_val_3, 15, 100 ))
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
#endwhile
pygame.quit()