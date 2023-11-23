import pygame


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE     = (   0,   0, 255)
YELLOW   = (255 , 255,   0)
PURPLE   = ( 150,   0, 150)
PINK     = ( 255, 192, 203)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

move_x = 0
move_y = 0


class Block(pygame.sprite.Sprite):
    def __init__(self, block_width, block_height, x_val, y_val) -> None:
        super().__init__()
        self.image = pygame.Surface([block_width, block_height])
        self.image.fill(BLACK)
        self.rect=self.image.get_rect()#Setthepositionoftheplayerattributes
        self.rect.x=x_val
        self.rect.y=y_val


class Pacman(pygame.sprite.Sprite):

    def __init__(self, lives, initial_x, initial_y) -> None:
        super().__init__()
        self.lives = lives
        self.speed = 1
        self.width = 10
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(YELLOW), 
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = initial_y

    def eatItem(self, item):
        if item == item.pellet:
            pass

        elif item == item.buff:
            pass

    def update(self):
        global move_x
        global move_y
        self.rect.x += move_x
        self.rect.y += move_y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            move_x = -1
            move_y = 0
        if keys[pygame.K_RIGHT]:
            move_x = 1
            move_y = 0
        if keys[pygame.K_UP]:
            move_x = 0
            move_y = -1
        if keys[pygame.K_DOWN]:
            move_x = 0
            move_y = 1
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
            

        
class Item(pygame.sprite.Sprite):

    def __init__(self, pellet, buff) -> None:
        super().__init__()
        self.pellet = pellet
        self.buff = buff


class Ghost(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

map =[[1,1,1,1,1,1,1,1,1,1], 
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,1], 
      [1,1,0,1,1,1,1,1,0,1], 
      [1,0,0,0,0,0,1,0,0,1],
      [1,0,1,1,1,0,1,0,0,1],
      [1,0,1,1,1,0,1,0,0,1],
      [1,0,1,1,1,0,1,0,0,1], 
      [1,0,0,0,0,0,0,0,0,1], 
      [1,1,1,1,1,1,1,1,1,1]]

all_sprites = pygame.sprite.Group()

player_group = pygame.sprite.Group()

for _ in range(1):
    pacman = Pacman(3, 10, 30)
    all_sprites.add(pacman)
    player_group.add(pacman)
pygame.display.set_caption("My Game")

 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    all_sprites.update()
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLUE)
 
    # --- Drawing code should go here
    


    all_sprites.draw(screen)





    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()