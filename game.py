import pygame

# initialize the pygame module
pygame.init()

#initialize game window size
display_window = pygame.display.set_mode((800, 600))


# Title and icon
pygame.display.set_caption('Python Invaders')
ramen_icon = pygame.image.load('./images/ramen.png')
pygame.display.set_icon(ramen_icon)

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_window.fill((0,0,0))
    pygame.display.update()