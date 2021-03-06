from GameObject import *
from locals import *
from pygame import *
class Enemy(GameObject):
    def __init__(self,x,y):
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        WIDTH = 32
        HEIGHT = 32
        COLOR = "#E32636"
        sprite.Sprite.__init__(self)
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.hero=0;
        self.round=GameObject(self.startX-250, self.startY-250, Surface((500, 500)))
        self.round.rect = Rect(self.startX-250,self.startY-250, 500,500)
        self.start = GameObject(self.startX - 250, self.startY - 250, Surface((500, 500)))
        self.start.rect = Rect(self.startX, self.startY, 500, 500)
    def way(self,target):
        left=right=up=down=0;
        if(target==0):
            target=self.start
        if(target!=0):
            if(target.rect.x>self.rect.x):
                right=1
            elif(target.rect.x<self.rect.x):
                left=1
            if(target.rect.y>self.rect.y):
                down=1
            elif(target.rect.y<self.rect.y):
                up=1
        return left,right,up,down
    def update(self,platforms,hero):
        left, right, up, down = 0, 0, 0, 0;
        self.active(hero)
        #left,right,up,down=self.way(self.hero)
        if left:
            self.xvel = -MOVE_SPEED
        if right:
            self.xvel = MOVE_SPEED
        if up:
            self.yvel = -MOVE_SPEED
        if down:
            self.yvel = MOVE_SPEED
        if not (right or left):
            self.xvel = 0
        if not (up or down):
            self.yvel = 0
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
    def collide(self,xvel,yvel,platforms):
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
    def active(self,hero):
        if(sprite.collide_rect(self.round,hero)):
            self.hero=hero
            #print('spotted!')
        else:
            self.hero=0;

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))