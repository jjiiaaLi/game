import pygame
import math
pygame.init()

screen = pygame.display.set_mode((1200, 900))
clock = pygame.time.Clock()

#objects
AAA_img = pygame.image.load('./images/AAA.png')
aircraft_img = pygame.image.load('./images/aircraft.png')
tree_img = pygame.image.load('./images/tree.png')
blast_img = pygame.image.load('./images/blast.png')
projectile_img = pygame.image.load('./images/projectile.png')

projectile_state = 'loaded'  # place holder for space command

def AAA():
    screen.blit(AAA_img,(400,820))

def aircraft(x,y):
    screen.blit(aircraft_img,(x,y))

def tree(x,y):
    screen.blit(tree_img,(x,y))

tree_x_list = [200,230,240,250,770,780,790,820]

def projectile(x,y):
    screen.blit(projectile_img,(x,y))

def blast(x,y):
    screen.blit(blast_img,(x,y))

running = True
while running:

    screen.fill((255,255,255))
    clock.tick(60)

    AAA()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                projectile_state = 'fire'
    for i in tree_x_list:
        tree(i,820)

    pygame.display.update()