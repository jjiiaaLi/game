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
enemy_x = 600
enemy_y = 40
enemy_delta_x = 2

def enemy(x,y):
    display_window.blit(enemy_img,(x,y))

# laser
laser_img = pygame.image.load('./images/laser.png')
laser_x = 0
laser_y = 0
laser_y_delta = -9
laser_state = 'ready'

def fire_laser(x,y):
    global laser_state
    laser_state = 'fire'
    display_window.blit(laser_img,( x + 18, y + 19 ))


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
    enemy(enemy_x, enemy_y)
    enemy_x += enemy_delta_x
    if enemy_x >740 or enemy_x < 20:
        enemy_delta_x *= -1
        enemy_y += 50

    if laser_state == 'fire':
        fire_laser(laser_x,laser_y)
        laser_y += laser_y_delta
        
    if laser_y < 0:
        laser_state = 'ready'


    pygame.display.update()
