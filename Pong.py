"""
##############################################################################################################################################################################################################

Copyright Disclaimer

The code below is copyrighted by the original author below:
https://pygame.readthedocs.io/en/latest/1_intro/intro.html
© Copyright 2019, Raphael Holzer Revision b84b643a.

I do not own this content and I am not affiliated with the original author in any way. 

I am simply using this content for educational purposes.

If you are the copyright holder of this content and you believe that I am infringing on your copyright,
please contact me and I will remove the content immediately.

##############################################################################################################################################################################################################
"""

import pygame
from colors import Colors
from pygame.locals import *
from pygamelib import *

# RED = (255,0,0)
# GREEN = (0,255,0)
# BLACK = (0, 0, 0)
# GRAY = (127, 127, 127)
# WHITE = (255, 255, 255)

class App:
    """Create a single-window app with multiple scenes"""
    
    def __init__(self):
        """Initialize pygame and the application"""
        pygame.init()
        flags=RESIZABLE
        App.screen=pygame.display.set_mode((640,240),flags)
        App.running=True
    
    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type==QUIT:
                    App.running=False
        pygame.quit()

"""
TO DO: REFACTOR THIS FOR SPECIFIC NEED BASED ON DOCS
"""
class Text:
    """Create a text object."""
    def __init__(self, text, pos, **options):
        self.text=text
        self.pos=pos
        self.fontname=None
        self.fontsize=72
        self.fontcolor=Color('black')
        self.set_font()
        self.render()
    
    def set_font(self):
        self.font=pygame.font.Font(self.fontname,self.fontsize)

    def render(self):
        self.img=self.font.render(self.text,True,self.fontcolor)
        self.rect=self.img.get_rect()
        self.rect.topleft=self.pos

class Ball:
    def __init__(self, pos, field, pad):
        self.pos=pos
        self.field=field
        self.pad=pad
        self.speed=[1,1]
        self.color=Colors.RED
        self.rect=pygame.Rect(pos,(20,20))
    
    def update(self):
        self.rect.move_ip(self.speed)

        if self.rect.left < self.field.rect.left:
            self.speed[0]=abs(self.speed[0])
        if self.rect.right > self.field.rect.right:
            self.speed[0]=-abs(self.speed[0])

        if self.rect.top < self.field.rect.top:
            self.speed[1]=abs(self.speed[1])
        if self.rect.bottom > self.field.rect.bottom:
            self.speed[1]=-abs(self.speed[1])

        if self.rect.collidedict(self.pad.rect):
            self.speed[0]=abs(self.speed[0])

    def draw(self):
        pygame.draw.rect(App.screen, self.color, self.rect, 0)

class Pad:
    def __init__(self, keys, field):
        self.keys=keys
        self.field=field
        self.speed=[0,0]
        self.v=5
        self.color=Colors.GREEN
        self.rect=pygame.Rect(self.field.rect.topleft, (10,50))
        self.rect.move_ip(10,0)
    
    def do(self, event):
        if event.type==KEYDOWN:
            if event.key==self.keys[0]:
                self.speed[1]=-self.v
            if event.ket==self.keys[1]:
                self.speed[1]=self.v
        elif event.type==KEYUP:
            self.speed[1]=0

    def update(self):
        self.rect.move_ip(self.speed)

        if self.rect.top < self.field.rect.top:
            self.rect.top=self.field.rect.top
        if self.rect.bottom > self.field.rect.bottom:
            self.rect.bottom=self.field.rect.bottom
    
    def draw(self):
        pygame.draw.rect(App.screen,self.color,self.rect,0)

class Field:
    def __init__(self, rect):
        self.color=Colors.WHITE
        self.bg_color=Colors.BLACK
        self.stroke=10
        self.rect=pygame.rect(rect)
    
    def draw(self):
        pygame.draw.rect(App.screen,self.color,self.rect,self.stroke)
        pygame.draw.rect(App.screen,self.bg_color,self.rect,0)

class PongDemo(App):
    """Play the game of Pong."""
    def __init__(self):
        super().__init__()
        Text('Pong',size=48)

        self.field=Field((200,10,400,200))
        self.pad=Pad((K_UP,K_DOWN), self.field)
        self.ball=Ball(self.field.rect.center,self.field,self.pad)
        self.bg_color=GRAY

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type==QUIT:
                    self.running=False
                    pygame.quit()
                
                self.pad.do(event)
            
            self.update()
            self.draw()
    
    def update(self):
        self.ball.update()
        self.pad.update()
    
    def draw(self):
        self.screen.fill(self.bg_color)
        self.field.draw()
        self.ball.draw()
        self.pad.draw()
        pygame.display.flip()

if __name__ == '__main__':

    PongDemo().run()
