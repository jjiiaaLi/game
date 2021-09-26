import pygame
import math
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

#objects
sight_img = pygame.image.load('./images/sight.png')
background = pygame.image.load('./images/background.jpg')
background_y = -4080
background_y_delta = .5
def sight():
    screen.blit(sight_img,(270,0))

bomb_state = 'ready'  # place holder for space command



running = True
while running:

    screen.fill((255,255,255))
    screen.blit(background,(0,background_y))
    background_y += background_y_delta
    clock.tick(60)

    sight()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bomb_state = 'pickle'
    

    pygame.display.update()