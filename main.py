from pygame import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption("Ping Pong")

clock = time.Clock()

runing = True
while runing:

    for ev in event.get():
        if ev.type == QUIT:
            runing = False
    
    clock.tick(FPS)
        
quit()