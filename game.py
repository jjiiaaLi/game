import pygame

# initialize the pygame module
pygame.init()

#initialize game window size
display_window = pygame.display.set_mode((800, 600))


# Title and icon
pygame.display.set_caption('Python Invaders')
ramen_icon = pygame.image.load('./images/ramen.png')
pygame.display.set_icon(ramen_icon)


#player
player_img = pygame.image.load('./images/player.png')
player_x = 370  # player initial position x axis
player_y = 480  # player initial position y axis

def player(x,y):  #  function to be called to place player on the screen
    display_window.blit(player_img,(x,yy))



# Game loop
running = True

while running:
    display_window.fill((0, 0, 0))  # draw the screen background


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:

            if event.key == pygame.K_RIGHT:
        
            
    
    player(player_x,player_y) # render the player image
    pygame.display.update()
