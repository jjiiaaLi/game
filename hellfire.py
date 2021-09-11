from typing import get_origin
import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1000,750))
clock = pygame.time.Clock()


#objects
helicopter_img = pygame.image.load('./hellfire_imgs/helicopter.png')
missile_img = pygame.image.load('./hellfire_imgs/projectile.png')
tree_img = pygame.image.load('./hellfire_imgs/tree.png')
tank_img = pygame.image.load('./hellfire_imgs/tank.png')
blast_img = pygame.image.load('./hellfire_imgs/blast.png')

def helicopter():
    screen.blit(helicopter_img, (0, 570))

def tree(x,y):
    screen.blit(tree_img, (x,y))

tank_x = 880
tank_y = 600

def tank(x,y):
    screen.blit(tank_img, (tank_x, tank_y))


missile_x = 33
missile_y = 580
missile_x_delta = 5
missile_y_delta = -2

ground = 600

def missile(x,y):
    screen.blit(missile_img, (missile_x,missile_y))



missile_state = 'unfired'

forest_x= [400,429,450,465,500,535,550,930,945]
forest_y = 600

def intercept(target_x, target_y, self_x,self_y):
    range_to_target = target_x - self_x
    alt_diff = target_y - self_y
    frames_to_x_intercept = (range_to_target / missile_x_delta)
    frames_to_y_intercept_for_intercept = (alt_diff / frames_to_x_intercept)

    return frames_to_y_intercept_for_intercept

running = True
while running:

    screen.fill((255,255,255))
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                missile_state = 'fired'



    helicopter()
    tank(tank_x, tank_y)
    
    for i in range(len(forest_x)):
        tree(forest_x[i],forest_y)

    if missile_state == 'fired':
        
        missile(missile_x,missile_y)
        missile_x += missile_x_delta
        missile_y += missile_y_delta
    
    if missile_x > 500 and missile_y > ground +4:
        missile_state = 'exploded'
        screen.blit(blast_img,(missile_x,missile_y))
        missile_x_delta=0
        missile_y_delta=0

    if missile_x > 70 and missile_x <120:
        missile_y_delta = -4

    if missile_x > 120 and missile_x < 200:
        missile_y_delta = -4.7

    if missile_x > 200 and missile_x < 270:
        missile_y_delta = -4.4

    if missile_x > 270 and missile_x < 310:
        missile_y_delta = -4.2

    if missile_x > 370 and missile_x < 500:
        missile_y_delta = 0
    
    # print(tank_x - missile_x, tank_y - missile_y)
    if missile_x > 500 and missile_state == 'fired':
        missile_y_delta = intercept(880  ,600 ,missile_x,missile_y)

    pygame.display.update()
