from typing import Any
from pygame import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption("Ping Pong")

clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, speed, wight, height, color):
        self.speed = speed
        self.color = color
        self.rect = Rect(x, y, wight, height)
    
    def draw(self):
        draw.rect(screen, self.color, self.rect)

class Ball(GameSprite):
    def __init__(self, x, y, speed, radius, color):
        self.color = color
        self.radius = radius
        self.speed_x = speed
        self.speed_y = speed
        super().__init__(x, y, speed, 2 * radius, 2 * radius, color)

    def draw(self):
        draw.circle(screen, self.color, self.rect.center, self.radius)
    
    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y

        if self.rect.y < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed_y = -1 * self.speed_y 

class Player(GameSprite):

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y = self.rect.y - self.speed
        if keys[K_DOWN] and self.rect.y < SCREEN_HEIGHT - self.rect.height:
            self.rect.y = self.rect.y + self.speed  

    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y = self.rect.y - self.speed
        if keys[K_s] and self.rect.y < SCREEN_HEIGHT - self.rect.height:
            self.rect.y = self.rect.y + self.speed  



player1 = Player(10, 200, 10, 30, 150, "red")
player2 = Player(760, 200, 10, 30, 150, "blue")
ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 5, 10, "white")

finish = False
runing = True
while runing:

    for ev in event.get():
        if ev.type == QUIT:
            runing = False

            
    screen.fill("black")

    if finish != True:
        # tu kreslime
        
        player1.draw()
        player2.draw()
        ball.draw()
        
        # updatujeme
        player2.update_right()
        player1.update_left()
        ball.update()

        #kolizie
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            ball.speed_x = -1 * ball.speed_x

        if ball.rect.x > SCREEN_WIDTH:
            finish = True
            #prehral pravy player
            # screen.blit(texobj, (x,y))
        
        if ball.rect.x < 0:
            finish = True
            #prehral lavy
            # screen.blit(texobj, (x,y))
        


    display.update()
    
    clock.tick(FPS)
        
quit()
