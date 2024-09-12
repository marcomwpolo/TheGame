import pygame, sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280/2
screen_height = 960/2
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game rectangles
ball = pygame.FRect(screen_width/2 - 15,screen_height/2 - 15,30.0,30.0)
player = pygame.FRect(screen_width - 20, screen_height/2 - 70, 10.0,140.0)
opponent = pygame.FRect(10.0, screen_height/2 - 70, 10.0, 140.0)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey, player)
    pygame.draw.rect(screen,light_grey, opponent)
    pygame.draw.ellipse(screen,light_grey, ball)

    # Updating the window
    pygame.display.flip()
    clock.tick()