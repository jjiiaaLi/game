import pygame
import random

# initialize the pygame module
pygame.init()

#initialize game window size
display_window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#background image
background_img = pygame.image.load('./images/background.png')


# Title and icon
pygame.display.set_caption('Python Invaders')
ramen_icon = pygame.image.load('./images/ramen.png')
pygame.display.set_icon(ramen_icon)


#player
player_img = pygame.image.load('./images/player.png')
player_x = 370  # player initial position x axis
player_y = 480  # player initial position y axis
player_delta_x = 0

def player(x,y):  #  function to be called to place player on the screen
    display_window.blit(player_img,(x,y))


#enemy
enemy_img = pygame.image.load('./images/enemy.png')
enemy_count = 3
last_hit = 0
enemy_x_list = []
enemy_y_list = []
enemy_x_change= []
enemy_y_change =[]

for i in range(enemy_count):
    enemy_x_list.append(random.randint(100, 700))
    enemy_y_list.append(random.randint(0, 200))
    enemy_x_change.append(2)
    enemy_y_change.append(50)



def enemy(x,y):
    display_window.blit(enemy_img,(x,y))

# laser
laser_img = pygame.image.load('./images/laser.png')
laser_x = 0
laser_y = 0
laser_y_delta = -10
laser_state = 'ready'

def fire_laser(x,y):
    global laser_state
    laser_state = 'fire'
    display_window.blit(laser_img,( x + 18, y + 19 ))


#hit
def hit(shot_x,shot_y,target_x,target_y):
    if shot_y < (target_y + 50) and shot_y > (target_y - 30) and shot_x > (target_x - 30) and shot_x < (target_x + 30):
        return True


# Game loop
running = True

while running:
    display_window.fill((0, 0, 0))  # draw the screen background
    display_window.blit(background_img,(0,0))

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_delta_x = -3
            if event.key == pygame.K_RIGHT:
                player_delta_x = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_delta_x = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                laser_state = 'fire'
                laser_x = player_x
                laser_y = player_y
                
    

    player(player_x,player_y) # render the player image
    player_x += player_delta_x

    #player border limit
    if player_x < 0 or player_x > 738:
        player_delta_x = 0

    #enemy initial enter

    for i in range(enemy_count):
        enemy_x = enemy_x_list[i]
        enemy_y = enemy_y_list[i]

        enemy(enemy_x, enemy_y)
        enemy_x_list[i] += enemy_x_change[i]

    for i in range(enemy_count):
        if enemy_x_list[i] > 740 or enemy_x_list[i] < 20:
            enemy_x_change[i] *= -1
            enemy_y_list[i] += 50
    

    if laser_state == 'fire':
        fire_laser(laser_x,laser_y)
        laser_y += laser_y_delta
        
    if laser_y < 0:
        laser_state = 'ready'
 

    #collision
    impact = False
    
    for i in range(enemy_count):
        if hit(laser_x,laser_y,enemy_x_list[i],enemy_y_list[i]):
            last_hit = i
            impact = True

    if impact:
        laser_state = 'ready'
        enemy_x_list[last_hit] = random.randint(100,700)
        enemy_y_list[last_hit] = random.randint(0,200)
            

    pygame.display.update()
