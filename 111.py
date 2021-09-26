import pygame
import math
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

#objects
sight_img = pygame.image.load('./images/sight.png')
background_img = pygame.image.load('./images/background.jpg')
blast_img = pygame.image.load('./images/blast.png')

def blast(x,y):
    screen.blit(blast_img,(x,y))

blast_x = 650
blast_y = 400
blast_y_delta = 0.7

count_to_blast = 640

def background(x,y):
    screen.blit(background_img,(x,y))
background_x = -900
background_x_delta = 0
background_y = -2080
background_y_delta = 0.7
def sight():
    screen.blit(sight_img,(0,0))

bomb_state = 'ready'  # place holder for space command
bomb_sight_rotate_count = 0

def ramen():
    screen.blit(ramen_img,(0,0))

running = True
while running:

    screen.fill((255,255,255))
    
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                background_x_delta = 0.6
                print('left')
            if event.key == pygame.K_RIGHT:
                background_x_delta = -0.6
                print('right')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print('stop')
                background_x_delta = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bomb_state = 'pickle'
                bomb_sight_rotate_count = 25

    background(background_x,background_y)
    background_x += background_x_delta
    background_y += background_y_delta

    sight()

    if bomb_state == 'pickle': 
        if bomb_sight_rotate_count > 0:
            background_y_delta = -15
            bomb_sight_rotate_count -= 1
        if bomb_sight_rotate_count == 0:
            background_y_delta = 0.7
        if count_to_blast >0:
            count_to_blast -= 1
    if count_to_blast == 0:
        blast(blast_x,blast_y)
        blast_y += blast_y_delta
    pygame.display.update()
