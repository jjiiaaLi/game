import pygame

pygame.init()

screen = pygame.display.set_mode((1000,750))
clock = pygame.time.Clock()


#objects
helicopter_img = pygame.image.load('./hellfire_imgs/helicopter.png')
missile_up_img = pygame.image.load('./hellfire_imgs/missile_up.png')
missile_down_img = pygame.image.load('./hellfire_imgs/missile_down.png')
missile_level_img = pygame.image.load('./hellfire_imgs/missile_level.png')
tree_img = pygame.image.load('./hellfire_imgs/tree.png')
tank_img = pygame.image.load('./hellfire_imgs/tank.png')

def helicopter():
    screen.blit(helicopter_img, (0, 570))

def tree(x,y):
    screen.blit(tree_img, (x,y))

def tank():
    screen.blit(tank_img, (900, 600))

missile_up_x = 37
missile_up_y = 584
missile_down_x = -50
missile_down_y = -50


missile_delta_x = 7
missile_down_delta_y = 2


def missile_up(x,y):
    screen.blit(missile_up_img,(x,y))
def missile_down(x,y):
    screen.blit(missile_down_img,(x,y))
def missile_level(x,y):
    screen.blit(missile_level_img,(x,y))

missile_state = 'unfired'

forest_x= [400,429,450,465,500,535,550]
forest_y = 600



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
    tank()
    missile_down(missile_down_x,missile_down_y)
    for i in range(len(forest_x)):
        tree(forest_x[i],forest_y)

    if missile_state == 'fired':
        missile_up(missile_up_x,missile_up_y)
        missile_up_x += 7
        missile_up_y += -3
        
    if missile_up_x >400 or missile_up_x <0:
        missile_down_x = missile_up_x
        missile_down_y = missile_up_y
        missile_down_x += missile_delta_x
        missile_down_y += 3
        missile_up_x = -50
        missile_up_y = -50
        
  

    pygame.display.update()
