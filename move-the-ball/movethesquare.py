allwhite= "allwhite.jpg"
black= "blackball.png"

import pygame, sys
from pygame.locals import*

pygame.init()
screen= pygame.display.set_mode((640,480),0,32)
background= pygame.image.load(allwhite).convert()
ball =pygame.image.load(black).convert_alpha()

x,y = 0,0
movex, movey = 0,0

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            if event.type == KEYDOWN:
                if event.key==K_LEFT:
                    movex=-1
                elif event.key==K_RIGHT:
                    movex=+1
                elif event.key==K_UP:
                    movey=-1
                elif event.key==K_DOWN:
                    movey=+1
            if event.type==KEYUP:
                if event.key==K_LEFT:
                    movex=0
                    if event.key==_KEY_RIGHT:
                        movex=0
                    elif event.key==KEY_UP:
                        movey=0
                        if event.key==KEY_DOWN:
                            movey=0
                        
        x+=movex
        y+=movey
x -= ball.get_width() /2 #/2 puts cursor in the middle of the image rather than a corner
y -= ball.get_height() /2

screen.blit(background,(0,0))

screen.blit(ball, (x,y))

pygame.display.update()
