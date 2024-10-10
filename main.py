import pygame, sys, random

# General setup
pygame.init()
clock = pygame.time.Clock()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
player_score = 0
opponent_score = 0

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai ():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom >ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1, -1))

# Setting up the main window
screen_width = 1280/2
screen_height = 960/2
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')
game_state = 1

# Game rectangles
opponent_score_text = my_font.render(str(opponent_score), False, (255, 255, 255))
player_score_text = my_font.render(str(player_score), False, (255, 255, 255))
ball = pygame.FRect(screen_width/2 - 15,screen_height/2 - 15,30.0,30.0)
player = pygame.FRect(screen_width - 20, screen_height/2 - 70, 10.0,140.0)
opponent = pygame.FRect(10.0, screen_height/2 - 70, 10.0, 140.0)
rectangle = pygame.FRect(121,121,121,121)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7

while True:
    # Handling input
    if game_state == 0:
        if ball.left <= 0:
            opponent_score += 1
        if ball.right >= screen.width:
            player_score += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 7
                if event.key == pygame.K_UP:
                    player_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 7
                if event.key == pygame.K_UP:
                    player_speed += 7


        ball_animation()
        player_animation()
        opponent_ai()
        # Visuals
        screen.fill(bg_color)
        pygame.draw.rect(screen,light_grey, player)
        pygame.draw.rect(screen,light_grey, opponent)
        pygame.draw.ellipse(screen,light_grey, ball)
        pygame.draw.aaline(screen,light_grey, (screen_width/2,0), (screen_width/2,screen_height))
        screen.blit(opponent_score_text, (screen_width/2-20, 0))
        screen.blit(player_score_text, (screen_width/2+10, 0))

    if game_state == 1:
        pygame.draw.rect(screen,light_grey, rectangle)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_state = 0

    # Updating the window
    pygame.display.flip()
    clock.tick(60)