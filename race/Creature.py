import pygame
from PIL import Image
import os
import math

class Creature(pygame.sprite.Sprite):
    def __init__(self,startX,startY,name,level,image_name,image = None):
        self.startX=startX
        super().__init__()
        self.startY=startY
        self.level = level
        self.rotation = 0
        self.vel = 20
        self.image_name = image_name
        if(image):
            self.image = image
        else:
            raise BaseException
        self.rect = image.get_rect()
        self.rect.x, self.rect.y = startX, startY
        self.name = name
    def get_damage(self):
        return 60+15*self.level
    def update(self,screen):
        self.draw(screen)
    def draw(self,screen, into_rect):
        screen.blit(self.image, (self.rect.x,self.rect.y), into_rect)

class Hero(Creature):
    def __init__(self,startX,startY,name,image_name,image = None):
        super().__init__(startX, startY, name, 1,image_name, image)
        self.level = 1
        # TO DO
        #  equipped = None
    def get_damage(self):
        # TO DO
        #  if equipped
        return 30+15*self.level;
    def update(self,screen, moving, rotation_turn):
        self.rotation += rotation_turn
        if(rotation_turn):
            self.rotate()
        if moving == 1:
            self.rect.x += self.vel * math.cos(self.rotation * (math.pi / 180))
            self.rect.y -= self.vel * math.sin(self.rotation * (math.pi / 180))
        if moving == -1:
            self.rect.x -= self.vel * math.cos(self.rotation * (math.pi / 180))
            self.rect.y += self.vel * math.sin(self.rotation * (math.pi / 180))
    def rotate(self):
        image = Image.open(os.path.join('data', self.image_name + '.png'))
        image_out = image.rotate(self.rotation)
        image_out.save(os.path.join('data', self.image_name + 't.png'))
        self.set_image(self.image_name + 't')
    def set_image(self,image):
        try:
            self.image=pygame.image.load(os.path.join('data',image+'.png'))
        except:
            print('UNABLE TO LOAD IMAGE '+image)
            raise EnvironmentError
