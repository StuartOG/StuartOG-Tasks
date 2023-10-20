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
    
    def __init__(self, s_width, s_height):
        super().__init__()

        self.width = s_width
        s_width = random.randrange(20, 25)
        self.height = s_height
        s_height = random.randrange(20, 25)
        self.image = pygame.Surface([s_width* 2, s_height * 2])
        pygame.draw.circle(self.image, BLACK, (s_width, s_height), 20)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, 750)
        self.rect.y = 0
        self.speed = 1 


    def update(self):
        if self.rect.y > 500:
            global over 
            over = True

        else:
            self.rect.y = self.rect.y + self.speed

        #end if

class Player(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length, initial_x):
        super().__init__()
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

class Bullet(pygame.sprite.Sprite):
    def __init__(self, s_width, s_height):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = s_width
        self.rect.centery = s_height
        
    def update(self):
        self.rect.y = self.rect.y - 3
        # Remove the bullet when it goes off the screen
        if self.rect.y < 0:
            self.kill()


        
# class Waves(pygame.sprite.Sprite):
#     def __init__ (self, wave):
#         super().__init__()
#         self.wave = wave
#         wave = 1

# def Waves():
#     level = 1
#     if len(invader_group) == 0:
#         level += 1
    



# end Class snow



# Global variables
x_val = 400

x_val2 = 350

over = False

game_over = "Game Over"
end = ""
text_font = pygame.font.SysFont(None, 30)
font = pygame.font.SysFont(None, 50)
level = 1

size = random.randrange(1,2)
s_width = random.randrange(20,25)
s_height = random.randrange(20,25)

all_sprites = pygame.sprite.Group()

player_group = pygame.sprite.Group()

invader_group = pygame.sprite.Group()

bullet_group = pygame.sprite.Group()

number_of_enemies = 10
for _ in range(number_of_enemies):
    flake = Snow(s_width, s_height)
    invader_group.add(flake)
    all_sprites.add(flake)

for _ in range(1):
    player = Player(40, 30, x_val2)
    player_group.add(player)
    all_sprites.add(player)

    


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = Bullet(player.rect.centerx, player.rect.top)
            bullet_group.add(bullet)
            all_sprites.add(bullet)


    hits = pygame.sprite.groupcollide(invader_group, bullet_group, True, True)

    keys = pygame.key.get_pressed()
    # --- Game logic should go here
    all_sprites.update()
    for bullet in bullet_group:
        bullet_group.update()
    # --- Drawing code should go here
    
    

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    level_count=font.render(str(level), True, BLACK)
    screen.blit(level_count, [400, 250])
     
    if len(invader_group) == 0:
        s_width = 30
        s_height  = 15 
        enemy = Snow(s_width, s_height)
        number_of_enemies += 3
        level += 1
        for _ in range(number_of_enemies):
            flake = Snow(s_width, s_height)
            invader_group.add(flake)
            all_sprites.add(flake) 

        all_sprites.add(enemy)
    
    invader_group.draw(screen)
    player_group.draw(screen)
    keys = pygame.key.get_pressed()
    bullet_group.draw(screen)
    bullet_group.update()

    if over == True:
        end = "game over"
        endmessage = screen.blit(end, [400, 250])
        pygame.display.flip()
        time.sleep(1)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)