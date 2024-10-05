import pygame
from init import game_display
from objekt import FONT, ball, player, opponent, ball_xd, ball_yd
from constans import *

def show_score(Surface, _str, color, which):
    str_obj = FONT.render(_str, True, color)
    position = list(str_obj.get_size())
    if which:
         position[0] = (WIDTH//2)-position[0]-20
    else:
          position[0] = (WIDTH//2)+20
    Surface.blit(str_obj, position)

def update_player(player, keys):
      if keys[pygame.K_UP] and player.top>=5:
        player.y-= PADDLE_SPEED
      if keys[pygame.K_DOWN] and player.bottom<=HEIGHT-5:
        player.y+=PADDLE_SPEED
      return player

def ball_direction(ball_yd, ball_xd):
      collision = False
      if ball.bottom >= HEIGHT or ball.top<=0:
          ball_yd *= -1
      if (ball.colliderect(player) ) or (ball.colliderect(opponent) ):
          ball_xd *= -1
          #collision = not collision
      return ball_yd, ball_xd

def score(opponent_score, player_score):
      if ball.right > WIDTH:
          opponent_score += 1
          ball.x ,ball.y = WIDTH//2-BALL_SIZE[0]//2,HEIGHT//2-BALL_SIZE[1]//2

      elif ball.left < 0:
          player_score +=1
          ball.x ,ball.y = WIDTH//2-BALL_SIZE[0]//2,HEIGHT//2-BALL_SIZE[1]//2
      return opponent_score, player_score



      


     
      