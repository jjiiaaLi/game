import pygame
import math
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

#objects
sight_img = pygame.image.load('./images/sight.png')
background_img = pygame.image.load('./images/background.jpg')
exp1_img = pygame.image.load('./images/exp/exp1.png')
exp2_img = pygame.image.load('./images/exp/exp2.png')
exp3_img = pygame.image.load('./images/exp/exp3.png')
exp4_img = pygame.image.load('./images/exp/exp4.png')
exp5_img = pygame.image.load('./images/exp/exp5.png')
exp6_img = pygame.image.load('./images/exp/exp6.png')




blast_x = 640
blast_y = 370
blast_y_delta = 0.7

count_to_blast = 600

def background(x,y):
    screen.blit(background_img,(x,y))
background_x = -900
background_x_delta = 0
background_y = -3900
background_y_delta = 0.7
def sight():
    screen.blit(sight_img,(0,0))

bomb_state = 'ready'  # place holder for space command
bomb_sight_rotate_count = 0



explosion_group = pygame.sprite.Group()

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
        if count_to_blast < 0 and count_to_blast >-12:
            screen.blit(exp1_img,(blast_x,blast_y))
            blast_y += blast_y_delta
        elif count_to_blast < -12 and count_to_blast > -14:
            screen.blit(exp4_img, (blast_x, blast_y))
            blast_y += blast_y_delta
        elif count_to_blast < -14 and count_to_blast > -16:
            screen.blit(exp5_img, (blast_x, blast_y))
            blast_y += blast_y_delta
        elif count_to_blast < -16 :
            screen.blit(exp6_img, (blast_x, blast_y))
            blast_y += blast_y_delta
        count_to_blast -= 1
   



    pygame.display.update()
