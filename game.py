import pygame

# initialize the pygame module
pygame.init()

#initialize game window size
display_window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

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
enemy_x = 0
enemy_y = 0

def enemy(x,y):
    display_window.blit(enemy_img,(x,y))

# Game loop
running = True

while running:
    display_window.fill((0, 0, 0))  # draw the screen background


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

    clock.tick(60)

    player(player_x,player_y) # render the player image
    player_x += player_delta_x

    enemy(enemy_x,enemy_y)

    if player_x < 0 or player_x > 738:
        player_delta_x = 0
    pygame.display.update()
