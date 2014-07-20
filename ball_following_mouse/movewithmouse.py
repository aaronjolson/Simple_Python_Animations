
import pygame, sys
from pygame.locals import*

pygame.init()
screen=pygame.display.set_mode((640,480),0,32)

bif="allwhite.jpg"
mif="blackball.png"

background=pygame.image.load(bif).convert()

mcurs=pygame.image.load(mif).convert_alpha()

while 1:
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()

    screen.blit((background), (0,0))

    x,y =pygame.mouse.get_pos()
    x-=mcurs.get_width()/2
    y-=mcurs.get_height()/2

    screen.blit(mcurs,(x,y))

    pygame.display.update()
