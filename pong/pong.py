import pygame
import sys
from constans import *
from init import *
from objekt import *
from fonctions import show_score, update_player, ball_direction, score

clock = pygame.time.Clock()

player_score = 0
opponent_score = 0
collision = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()     
    player = update_player(player, keys)
    
    
    ball_yd, ball_xd = ball_direction(ball_yd, ball_xd)
    
    ball.x += ball_xd
    ball.y += ball_yd

    opponent_score, player_score = score(opponent_score, player_score)
    if keys[pygame.K_SPACE]:
        if keys[pygame.K_s]:
            opponent.y += PADDLE_SPEED
        if keys[pygame.K_w]:
            opponent.y -= PADDLE_SPEED
    else:
        if opponent.center[1] < ball.center[1] and  opponent.bottom < HEIGHT:
            opponent.y += PADDLE_SPEED
        elif opponent.center[1] > ball.center[1] and opponent.top > 0:
            opponent.y -= PADDLE_SPEED


    game_display.fill((112,146,190))
    show_score(game_display, str(opponent_score), WHITE, True)
    show_score(game_display, str(player_score), WHITE, False)
    pygame.draw.rect(game_display, WHITE, player)
    pygame.draw.rect(game_display, WHITE, opponent)
    pygame.draw.ellipse(game_display, WHITE,ball)
    pygame.draw.line(game_display,WHITE,(WIDTH//2,0),(WIDTH//2,HEIGHT))
    
    pygame.display.update()
    clock.tick(60)