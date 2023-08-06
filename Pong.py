import pygame
from pygame.locals import *
from pygamelib import *

class Ball:
    def __init__(self, pos, field, pad):
        self.pos=pos
        self.field=field
        self.pad=pad
        self.speed=[1,1]
        self.color=RED
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
        self.color=GREEN
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
        self.color=WHITE
        self.bg_color=BLACK
        self.stroke=10
        self.rect=pygame.rect(rect)
    
    def draw(self):
        pygame.draw.rect(App.screen,self.color,self.rect,self.stroke)
        pygame.draw.rect(App.screen,self.bg_color,self.rect,0)