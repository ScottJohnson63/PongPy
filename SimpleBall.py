"""
##############################################################################################################################################################################################################

Copyright Disclaimer

The code below is copyrighted by the original author below:
(https://pygame.readthedocs.io/en/latest/1_intro/intro.html / © Copyright 2019, Raphael Holzer Revision b84b643a.)

I do not own this content and I am not affiliated with the original author in any way. 

I am simply using this content for educational purposes.

If you are the copyright holder of this content and you believe that I am infringing on your copyright,
please contact me and I will remove the content immediately.

##############################################################################################################################################################################################################
"""

import pygame
from pygame.locals import *
from colors import Colors

size=640,320
width,height=size
Colors.GREEN=(150,255,150)

pygame.init()
screen=pygame.display.set_mode(size)
running=True

ball=pygame.image.load("ball.gif")
rect=ball.get_rect()
speed=[2,2]

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        rect=rect.move(speed)
        if rect.left < 0 or rect.right > width:
            speed[0] = -speed[0]
        if rect.top < 0 or rect.bottom > height:
            speed[1] = -speed[1]
        screen.fill(Colors.GREEN)
        pygame.draw.rect(screen,Colors.RED,rect,1)
        screen.blit(ball,rect)
        pygame.display.update()

pygame.quit()