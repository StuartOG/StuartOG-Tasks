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
score = 0
text_font = pygame.font.SysFont(None, 30)
font = pygame.font.SysFont(None, 30)



class Pacman(pygame.sprite.Sprite):

    def __init__(self, lives, initial_x, initial_y) -> None:
        super().__init__()
        self.lives = lives
        self.speed = 1
        self.width = 10
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(PINK), 
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = initial_y

    def eatItem(self, item):
        global score
        if isinstance(item, Coin):
            score += 1
            item.kill()

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

        wall_collision = pygame.sprite.spritecollide(self, wall_list, False)
        for wall in wall_collision:
            if move_x > 0:
                self.rect.right = wall.rect.left - 1 
                move_x = 0
            elif move_x < 0:
                self.rect.left = wall.rect.right + 1
                move_X = 0
            if move_y > 0:
                self.rect.bottom = wall.rect.top - 1
                move_y = 0
            elif move_y < 0:
                self.rect.top = wall.rect.bottom + 1
                move_y = 0
            
        coin_collision = pygame.sprite.spritecollide(self, coin_list, False)
        for coin in coin_collision:
            pacman.eatItem(coin)

        ghost_collision = pygame.sprite.spritecollide(self, ghost_list, False)
        for ghost in ghost_collision:
            pass
        
class Item(pygame.sprite.Sprite):

    def __init__(self, pellet, buff) -> None:
        super().__init__()
        self.pellet = pellet
        self.buff = buff


class Ghost(pygame.sprite.Sprite):
    def __init__(self, width, height, G_colour, G_xval, G_yval) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.colour = G_colour   
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()  
        self.rect.x = G_xval
        self.rect.y = G_yval
map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
class Block(pygame.sprite.Sprite):
    def __init__(self ,B_colour , width , height, B_xval, B_yval):
        super().__init__()   
        self.width = width
        self.height = height
        self.colour = B_colour   
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()  
        self.rect.x = B_xval
        self.rect.y = B_yval
        
    def update(self):
        self = self
    

class Coin(pygame.sprite.Sprite):
    def __init__(self, C_colour, width, height, C_xval, C_yval) -> None:
        super().__init__()
        self.colour = C_colour
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()  
        self.rect.x = C_xval
        self.rect.y = C_yval


all_sprites = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
player_group = pygame.sprite.Group()
coin_list = pygame.sprite.Group()
ghost_list = pygame.sprite.Group()

for y in range(15):
    for x in range(20):
        if map[y][x] == 1:
            my_wall = Block(WHITE ,20 , 20 , x*20 , y*20)
            wall_list.add(my_wall)
            all_sprites.add(my_wall)


for y in range(15):
    for x in range(20):
        if map[y][x] == 2:
            my_ghost = Block(GREEN ,15 , 15 , x*20 , y*20)
            ghost_list.add(my_ghost)
            all_sprites.add(my_ghost)


# for y in range(15):
#     for x in range(20):
#         if map[y][x] == 0:
#             my_coin = Coin(YELLOW, 15, 15, x*20, y*20)
#             coin_list.add(my_coin)
#             all_sprites.add(my_coin)

for _ in range(1):
    pacman = Pacman(3, 20, 30)
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

    realscore = score 
    score_count = font.render("Score Count: " + str(realscore), True, BLACK)
    # endmessage = font.render(end, True, WHITE)
    # screen.blit(endmessage, [271,103])
    screen.blit(score_count, [200,4])




    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()