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
# from colors import Colors

class Colors:
    BLACK=(0,0,0)
    GRAY=(127,127,127)
    WHITE=(255,255,255)
    RED=(255,0,0)
    GREEN=(0,255,0)
    BLUE=(0,0,255)
    YELLOW=(255,255,0)
    CYAN=(0,255,255)
    MAGENTA=(255,0,255)

pygame.init()
screen=pygame.display.set_mode((640,240))

key_to_color={
    K_k:Colors.BLACK,
    K_r:Colors.RED,
    K_g:Colors.GREEN,
    K_b:Colors.BLUE,
    K_y:Colors.YELLOW,
    K_c:Colors.CYAN,
    K_m:Colors.MAGENTA,
    K_w:Colors.WHITE
}

caption="Select a background color"
pygame.display.set_caption(caption)
running=True
background=Colors.GRAY
while running:
    for event in pygame.event.get():
        # print(event)
        if event.type==pygame.QUIT:
            running=False
        if event.type==KEYDOWN:
            if event.key in key_to_color:
                background=key_to_color[event.key]
                # caption='background color = ' +str(background)
                # pygame.display.set_caption(caption)

    screen.fill(background)
    pygame.display.flip()

pygame.quit()