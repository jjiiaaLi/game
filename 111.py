import pygame
import math
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

#objects
sight_img = pygame.image.load('./images/sight.png')
background_img = pygame.image.load('./images/background.jpg')
blast_img = pygame.image.load('./images/blast.png')

class Explosion(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1,6):
            img = pygame.image.load(f'./images/explosion/exp{num}.png')
            #scale with img = pygame.transform.scale(img,(100,100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.counter = 0

        

    
    def update(self):
        explosion_speed = 4
        #update explosion animation
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) -1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        #if animation is complete, reset animation index
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()

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
background_y = -1080
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

    explosion_group.draw(screen)
    explosion_group.update()

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
