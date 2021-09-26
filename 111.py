import pygame
import math
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

#objects
sight_img = pygame.image.load('./images/sight.png')
background_img = pygame.image.load('./images/background.jpg')
ramen_img = pygame.image.load('./images/ramen.png')

def background(x,y):
    screen.blit(background_img,(x,y))
background_x = -900
background_x_delta = 0
background_y = -4080
background_y_delta = 0.7
def sight():
    screen.blit(sight_img,(0,0))

bomb_state = 'ready'  # place holder for space command

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

    background(background_x,background_y)
    background_x += background_x_delta
    background_y += background_y_delta

    sight()


    pygame.display.update()
