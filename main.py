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

player1 = GameSprite(10, 200, 5, 30, 150, "red")
player2 = GameSprite(760, 200, 5, 30, 150, "blue")

runing = True
while runing:

    for ev in event.get():
        if ev.type == QUIT:
            runing = False

    player1.draw()
    player2.draw()
    
    display.update()
    
    clock.tick(FPS)
        
quit()
