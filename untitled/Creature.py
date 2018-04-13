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
        self.vel = 5
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
        self.items = []
        self.health =40
        self.damage = 30
        self.weapon = None
        # TO DO
        #  equipped = None
    def get_damage(self):
        # TO DO
        #  if equipped
        return 30+15*self.level;
    def update(self,screen, moving, rotation_turn, items):
        self.rotation += rotation_turn
        if(rotation_turn):
            self.rotate()
        if moving == 1:
            self.rect.x += self.vel * math.cos(self.rotation * (math.pi / 180))
            self.rect.y -= self.vel * math.sin(self.rotation * (math.pi / 180))
        if moving == -1:
            self.rect.x -= self.vel * math.cos(self.rotation * (math.pi / 180))
            self.rect.y += self.vel * math.sin(self.rotation * (math.pi / 180))
        for item in items:
            if pygame.sprite.collide_rect(self, item):
                self.items.append(item)
                items.remove(item)
    def rotate(self):
        image = Image.open(os.path.join('data', self.image_name + '.png'))
        image_out = image.rotate(self.rotation)
        image_out.save(os.path.join('data', self.image_name + 't.png'))
        self.set_image(self.image_name + 't')
        self.rect.width, self.rect.height = self.image.get_width(), self.image.get_height()
    def set_image(self,image):
        try:
            self.image=pygame.image.load(os.path.join('data',image+'.png'))
        except:
            print('UNABLE TO LOAD IMAGE '+image)
            raise EnvironmentError

    def get_inventory(self):
        return self.items
