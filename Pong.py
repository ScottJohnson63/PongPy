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
