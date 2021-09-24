import pygame
import math
pygame.init()

screen = pygame.display.set_mode((1000, 750))
clock = pygame.time.Clock()

#objects
launcher_img = pygame.image.load('./images/launcher.png')
aircraft_img = pygame.image.load('./images/aircraft.png')
tree_img = pygame.image.load('./images/tree.png')
blast_img = pygame.image.load('./images/blast.png')
projectile_img = pygame.image.load('./images/projectile.png')
