import pygame
import sys
import random

class Game:
    space = pygame.image.load("./assets/s.png")
    color_g = random.randint(0,253)
    color_r = random.randint(0,253)
    color_b = random.randint(0,253)
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((1200,600))
        pygame.display.set_caption("Game")
        self.player_score = 0
        self.number = 49
        self.super_ball_height = 0
        self.tow = 2
        self.tow1 = 2
        self.rnd = random.randint(0,1150)
        self._rnd = random.randint(20,1180)
        self.font = pygame.font.Font(None,28)
        self._font = pygame.font.Font(None,100)
        self.player = pygame.Rect(1200//2-50,550,150,20)
        self.ball = pygame.Rect(1200//2-10,600//2-10,30,30)
        self.ball_speed = 4
        self.xd = self.ball_speed
        self.yd = self.ball_speed
        self.width = 60
        self.height = 20
        self._width = random.randint(0,60)
        self._height = 20
        self.height_ = -80
        self.state = True
        self.true = True
        self.true2 = True
        self.true1 = False
        self.false = False
        self.down = 20
        self.kill_height = 0
        self.counter = 0
        self.slicer = 1000
        
        self.clock = pygame.time.Clock()
        self.run()
    
    def rect_enmy(self,width,height):
        self.enmy = [[pygame.Rect(width-60,height,50,30)],
                [pygame.Rect(width,height,50,30)],
                [pygame.Rect(width+60,height,50,30)],
                [pygame.Rect(width+120,height,50,30)],
                [pygame.Rect(width+180,height,50,30)],
                [pygame.Rect(width+240,height,50,30)],
                [pygame.Rect(width+300,height,50,30)],
                [pygame.Rect(width+360,height,50,30)],
                [pygame.Rect(width+420,height,50,30)],
                [pygame.Rect(width+480,height,50,30)],
                #[pygame.Rect(width+540,height,50,30)],
                #[pygame.Rect(width+600,height,50,30)],
                [pygame.Rect(width+660,height,50,30)],
                [pygame.Rect(width+720,height,50,30)],
                [pygame.Rect(width+780,height,50,30)],
                [pygame.Rect(width+840,height,50,30)],
                [pygame.Rect(width+900,height,50,30)],
                [pygame.Rect(width+960,height,50,30)],
                [pygame.Rect(width+1020,height,50,30)],
                [pygame.Rect(width+1080,height,50,30)],
                [pygame.Rect(width+1140,height,50,30)]
               ]
    def generad(self,width,height):
        self.rects = []
        self.enm = [[pygame.Rect(width-60,height,50,30)],
                [pygame.Rect(width,height,50,30)],
                [pygame.Rect(width+60,height,50,30)],
                [pygame.Rect(width+120,height,50,30)],
                [pygame.Rect(width+180,height,50,30)],
                [pygame.Rect(width+240,height,50,30)],
                [pygame.Rect(width+300,height,50,30)],
                [pygame.Rect(width+360,height,50,30)],
                #[pygame.Rect(width+420,height,50,30)],
                [pygame.Rect(width+480,height,50,30)],
                [pygame.Rect(width+540,height,50,30)],
                [pygame.Rect(width+600,height,50,30)],
                [pygame.Rect(width+660,height,50,30)],
                [pygame.Rect(width+720,height,50,30)],
                [pygame.Rect(width+780,height,50,30)],
                [pygame.Rect(width+840,height,50,30)],
                #[pygame.Rect(width+900,height,50,30)],
                [pygame.Rect(width+960,height,50,30)],
                [pygame.Rect(width+1020,height,50,30)],
                [pygame.Rect(width+1080,height,50,30)],
                [pygame.Rect(width+1140,height,50,30)]
               ]
            
    def _player(self,surface,player):
        pygame.draw.rect(surface,(255,255,255),player)

    def show_score(self):
        self._str = self.font.render(str(self.player_score),True,'red')
        self.pos = list(self._str.get_size())
        self.pos[0] = self.player.x
        self.pos[1] = self.player.y
        self.game_display.blit(self._str,self.pos)

    def score(self):
        self.player_score +=1

    def update_player(self,player,key):
        self.speed1 = 14
        if key[pygame.K_RIGHT] and player.right<1190 and self.true2:
            player.x += self.speed1
        elif key[pygame.K_LEFT] and player.left>10 and self.true2:
            player.x -= self.speed1
        if key[pygame.K_DOWN] and self.true2:
            self.true = True
            self.false = False
            self.state = False
            self.yd +=1
        return player    
    
    def rect(self,surface,enmy,enm,color_g,color_r,color_b):
        for rect in enmy:
            for i in rect:
                self.rects.append(pygame.draw.rect(surface,(color_g,color_r,color_b),i))
            if self.width<-1200 or self.width == -1200:
                self.height = random.randint(0,40)
                self.width = 60
                self.yd += 1
                self.down = 30
                self.score()
                self.number = 30
                self.false = False
                self.true = True
                self.state = False

        for rect in enm:
            for i in rect:
                if self.height > 80:
                    pygame.draw.rect(surface,(color_b,color_g,color_r),i)
                if self._width > 1250:
                    self._height = 100
                    self._width = 60
                    self.yd += 1
                    self.down = 30
                    self.false = False
                    self.true = True
                    self.state = False
                    self.yd *= -1
                    self.score()
                    self.number = random.randint(0,100)-2
        if self.number >50:
            self.super_ball=pygame.Rect(self.rnd,self.super_ball_height,40,40)
            self.super_ball_height += self.tow
            pygame.draw.ellipse(self.game_display,'orange',self.super_ball)  
            if self.super_ball.colliderect(self.player):
                self.ball = pygame.Rect(600,300,40,40) 
                self.tow = 2
                self.remove = -120
                for rect in self.enmy:
                    for i in rect:
                        self.remove_enmy()
        if self.number<49:
            self.kill = pygame.Rect(self._rnd,self.kill_height,10,20)
            self.kill_height += self.tow1
            pygame.draw.rect(self.game_display,'orange',self.kill)
            if self.kill.colliderect(self.player):
                self.tow1 = 0
                if self.true1 == True:
                    self.tow1 = -2
                if self.key[pygame.K_RIGHT] and self.player.right < 1190:
                    self._rnd += self.speed1
                elif self.key[pygame.K_LEFT] and self.player.left>10 and self._rnd>20:
                    self._rnd -= self.speed1
                elif self.key[pygame.K_SPACE]:
                    self.true1 = True
            for rect in self.enmy:
                for i in rect:
                    if self.kill.colliderect(i) and self.true1 == True:
                        self.remove_enmy()
            for rect in self.enm:
                for i in rect:
                    if self.kill.colliderect(i) and self.true1 == True:
                        self.remove_enm()

    def ball_direction(self):
        self.ball.x += self.xd
        self.ball.y += self.yd
        if self.ball.left<=0:
            self.xd = -self.xd
        if self.ball.right>1200:
            self.xd = -self.xd
        if self.ball.top <= 5:
            self.yd *= -1
            self.state = False
            self.true = True
            self.false = False
        if (self.ball.colliderect(self.player) and self.true):
            self.state=False
            self.true = False
            self.false = False
            self.xd *= +1
            self.yd *= -1
            self.height = self.height+self.down
            if self.width<300:
                self._height = self._height+20

        for rect in self.enmy:
            for i in rect:
                if self.ball.colliderect(i) and self.state == False:
                    self.state = True
                    self.true = True
                    self.false = False
                    self.yd *= -1
                    self.xd *= +1
                    self.color_g = random.randint(0,253)
                    self.color_r = random.randint(0,253)
                    self.color_b = random.randint(0,253)
                    self.score()
                    self.remove_enmy()
                if self.ball.top < i.y-100 and self.ball.left < i.x:
                    self.state = False
        for rect in self.enm:
            for i in rect:
                if self.ball.colliderect(i) and self.false == False:
                    self.true = True
                    self.state = False
                    self.false = True
                    self.color_g = random.randint(0,253)
                    self.color_r = random.randint(0,253)
                    self.color_b = random.randint(0,253)
                    self.xd *= +1
                    self.yd *= -1
                    self.score()
                    self.remove_enm()

    def remove_enmy(self):
        self.remove = -60
        self.width += self.remove

    def remove_enm(self):
        self._width -= self.remove

    def font_game_over(self):
        self.str_obj = self._font.render("Game Over",True,'red')
        position = list(self.str_obj.get_size())
        position[0] = 400
        position[1] = 270
        self.game_display.blit(self.str_obj,position)

    def game_over(self):
        for rect in self.enmy:
            for i in rect:
                if i.bottom > self.player.bottom or self.ball.y > self.player.bottom:
                    self.font_game_over()
                    self.yd = 0
                    self.xd = 0 
                    self.tow = 0  
                    self.tow1 = 0
                    self.true2 = False
        for rect in self.enm:
            for i in rect:
                if i.bottom>self.player.bottom or  self.ball.y > self.player.bottom:
                    self.font_game_over()
                    self.yd = 0
                    self.xd = 0
                    self.tow = 0
                    self.tow1 = 0
                    self.true2 = False
    def run(self):
        while True:
            self.game_display.fill((70,70,70))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.game_display.blit(self.space,(-200,-100))
            pygame.draw.ellipse(self.game_display,'orange',self.ball)
            self.key = pygame.key.get_pressed()
            self.player=self.update_player(self.player,self.key)
            self._player(self.game_display,self.player)
            self.rect_enmy(self.width,self.height)
            self.generad(self._width,self._height-100)
            self.rect(self.game_display,self.enmy,self.enm,self.color_g,self.color_r,self.color_b)
            self.ball_direction()
            self.show_score()
            pygame.draw.line(self.game_display,'white',(0,569),(1200,569))
            self.game_over()
            
            pygame.display.update()
            self.clock.tick(60)
