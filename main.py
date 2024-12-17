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

def opponent_animation():
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

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
    global ball_speed_x, ball_speed_y, opponent_score, player_score
    if ball.left <= 0:
        player_score += 1
    if ball.right >= screen.width:
        opponent_score += 1
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1, -1))

def do_the_game(ai_is_on = True):
    global player_speed, opponent_speed, game_state
    if ai_is_on:
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

        if player_score == 11:
            game_state = -1
        if opponent_score == 11:
            game_state = -2

        ball_animation()
        player_animation()
        opponent_ai()
        opponent_speed = 7
        # Visuals
        screen.fill(bg_color)
        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
        opponent_score_text = my_font.render(str(opponent_score), False, (255, 255, 255))
        player_score_text = my_font.render(str(player_score), False, (255, 255, 255))
        screen.blit(opponent_score_text, (0, 0))
        screen.blit(player_score_text, (screen_width - 15, 0))
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 7
                if event.key == pygame.K_UP:
                    player_speed -= 7
                if event.key == pygame.K_s:
                    opponent_speed += 7
                if event.key == pygame.K_w:
                    opponent_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 7
                if event.key == pygame.K_UP:
                    player_speed += 7
                if event.key == pygame.K_s:
                    opponent_speed -= 7
                if event.key == pygame.K_w:
                    opponent_speed += 7


        if player_score == 11:
            game_state = -4
        if opponent_score == 11:
            game_state = -5

        ball_animation()
        player_animation()
        opponent_animation()
        # Visuals
        screen.fill(bg_color)
        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
        opponent_score_text = my_font.render(str(opponent_score), False, (255, 255, 255))
        player_score_text = my_font.render(str(player_score), False, (255, 255, 255))
        screen.blit(opponent_score_text, (0, 0))
        screen.blit(player_score_text, (screen_width - 15, 0))

# Setting up the main window
screen_width = 1280/2
screen_height = 960/2
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')
game_state = 1

# Game rectangles
ball = pygame.FRect(screen_width/2 - 15,screen_height/2 - 15,30.0,30.0)
player = pygame.FRect(screen_width - 20, screen_height/2 - 70, 10.0,140.0)
opponent = pygame.FRect(10.0, screen_height/2 - 70, 10.0, 140.0)
rectangle = pygame.FRect(121,121,121,121)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 0

while True:
    # Handling input
    if game_state == -5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        left_text = my_font.render("Left Player won!", False, (255, 255, 255))
        screen.blit(left_text, (screen_width / 2 - 50, screen_height / 2 - 50))

    if game_state == -4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        right_text = my_font.render("Right Player Won!", False, (255, 255, 255))
        screen.blit(right_text, (screen_width / 2 - 50, screen_height / 2 - 50))

    if game_state == -3:
        do_the_game(ai_is_on=False)

    if game_state == -2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        lose_text = my_font.render("You Lost :(", False, (255, 255, 255))
        screen.blit(lose_text, (screen_width/2-50, screen_height/2-50))

    if game_state == -1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        win_text = my_font.render("You Won! :)", False, (255, 255, 255))
        screen.blit(win_text, (screen_width/2-50, screen_height/2-50))


    if game_state == 0:
        do_the_game()

    if game_state == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_state = 0
                elif event.key == pygame.K_m:
                    game_state = -3
        title_text = my_font.render("Pong!", False, (255, 255, 255))
        screen.blit(title_text, (screen_width / 2 - 20, 0))
        play_text = my_font.render("Press Enter/Return Key To Begin...", False, (255, 255, 255))
        screen.blit(play_text, (screen_width / 2 - 155, 300))
        two_player_text = my_font.render("Press 'm' Key To Begin in 2 player mode...", False, (255, 255, 255))
        screen.blit(two_player_text, (screen_width / 2 - 155, 350))


    # Updating the window
    pygame.display.flip()
    clock.tick(60)