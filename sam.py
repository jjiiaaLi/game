import pygame
import math
pygame.init()

screen = pygame.display.set_mode((1000,750))
clock = pygame.time.Clock()

#objects
launcher_img = pygame.image.load('./images/launcher.png')
aircraft_img = pygame.image.load('./images/aircraft.png')
tree_img = pygame.image.load('./images/tree.png')
blast_img = pygame.image.load('./images/blast.png')
projectile_img = pygame.image.load('./images/projectile.png')


def launcher():
    screen.blit(launcher_img,(90,650))


def aircraft(x,y):
    screen.blit(aircraft_img, (x,y))



def tree(x,y):
    screen.blit(tree_img,(x,y))

trees= [30,50,70,115, 128, 145, 445,470,500,520,550,570,590,625,640,880,910,940,]
tree_y = 650

def blast(x,y):
    screen.blit(blast_img, (x,y))

def projectile(x,y):
    screen.blit(projectile_img,(x,y))

projectile_state = 'ready'

aircraft_x = 990
aircraft_y = 80
aircraft_x_delta = -1.5
aircraft_y_delta = 0


projectile_x = 100
projectile_y = 650
projectile_x_delta = 0
projectile_y_delta = -2.5

def intercept_x():
    
    x_range = (aircraft_x - projectile_x)
    y_range = (projectile_y - aircraft_y)
    
    # lead_amount = math.floor(x_range * 0.2)
    
    # new_x_range = x_range - lead_amount

    # frames_to_target = (math.sqrt(pow(x_range,2)+pow(y_range,2)))/abs(projectile_y_delta)
    frames_to_target = x_range / 2.5

    x = (x_range / frames_to_target)
    # y = -(y_range / frames_to_target)
    return round(x,5)
   
# def intercept_y():

#     x_range = (aircraft_x - projectile_x)
#     y_range = (projectile_y - aircraft_y)

#     frames_to_target = (math.sqrt(pow(x_range, 2)+pow(y_range, 2)))/abs(projectile_y_delta)

#     # y = -(y_range/frames_to_target)
#     print(y_range,frames_to_target)
#     # return round(y,4)

running = True
while running:

    screen.fill((255,255,255))
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                projectile_state = 'fired'

    for i in range(len(trees)):
        tree(trees[i], tree_y)

    launcher()

    aircraft(aircraft_x,aircraft_y)
    aircraft_x += aircraft_x_delta
    aircraft_y += aircraft_y_delta

    if projectile_state == 'fired':
        projectile(projectile_x,projectile_y)
       
        projectile_x += projectile_x_delta
        projectile_y += projectile_y_delta

    if projectile_y < 600:
        x_course=intercept_x()
        projectile_x_delta= x_course
        # y_course= intercept_y()
        # projectile_y_delta = y_course

        
        # print(y_course)

    

    pygame.display.update()
