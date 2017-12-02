from GameObject import GameObject
from pygame import *

MOVE_SPEED = 16


class Hero(GameObject):
    def __init__(self,source,x,y):
        #super().__init__(source,x,y)
        self.xvel=0
        self.yvel=0
        self.startX = x
        self.startY = y
        self.mouse = mouse
        self.attack_cooldown=0
        WIDTH = 32
        HEIGHT = 32
        COLOR = "#888888"
        sprite.Sprite.__init__(self)
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect =Rect(x,y,WIDTH,HEIGHT)
        self.moveable=1;
        self.disable_time=0;
        self.attack = GameObject(x, y, Surface((WIDTH +  500, HEIGHT + 500)))
        self.attack.image.fill(Color(COLOR))
        self.attack.rect = Rect(x-50, y-50, 500, 500)
    def update(self,left,right,up,down,platforms,enemies):
        #print(left,right,up,down)
        if(self.moveable):
            if left:
                self.xvel= -MOVE_SPEED
            if right:
                self.xvel= MOVE_SPEED
            if up:
                self.yvel= -MOVE_SPEED
            if down:
                self.yvel= MOVE_SPEED
            if not (right or left):
                self.xvel=0
            if not (up or down):
                self.yvel=0
        if(self.moveable == 0 and self.disable_time>0):
            self.disable_time-=1
        else:
            self.moveable=1
        if(self.attack_cooldown>0):
            self.attack_cooldown-=1
        self.rect.x += self.xvel
        self.attack.rect.x += self.xvel
        self.collide(self.xvel,0,platforms,enemies)
        self.rect.y += self.yvel
        self.attack.rect.y +=self.yvel
        self.collide(0,self.yvel,platforms,enemies)
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))
    def collide(self,xvel,yvel,platforms,enemies):
        for p in platforms:
            if sprite.collide_rect(self,p):
                if(xvel>0):
                    self.rect.right=p.rect.left
                if(xvel<0):
                    self.rect.left=p.rect.right
                if(yvel>0):

                    self.rect.bottom=p.rect.top
                if(yvel<0):

                    self.rect.top=p.rect.bottom
        for e in enemies:
            if self.attack.rect.contains(e):
                #if (self.mouse.get_pressed()[0] == True and not self.attack_cooldown>0):
                print('Attack!')
                self.attack_cooldown=10
            if (sprite.collide_rect(self,e) and self.moveable==True):
                if(e.rect.left==self.rect.left):
                    self.moveable=0
                    self.xvel = -MOVE_SPEED * 2
                    self.disable_time = 5
                if (e.rect.right == self.rect.right):
                    self.moveable=0
                    self.xvel = MOVE_SPEED * 2
                    self.disable_time = 5
                if (e.rect.bottom == self.rect.bottom):
                    self.moveable=0
                    self.yvel = -MOVE_SPEED * 2
                    self.disable_time = 5
                if (e.rect.top == self.rect.top):
                    self.moveable=0
                    self.yvel = MOVE_SPEED * 2
                    self.disable_time = 5
    def die(self):
        time.wait(500)
        self.teleporting(self.startX,self.startY)
    def teleporting(self,goX,goY):
        self.rect.x=goX
        self.rect.y=goY