from GameObject import GameObject
from pygame import *

WALL_WIDTH = 32;
WALL_HEIGHT = 32;
WALL_COLOR ="#FF6262"

class Wall(GameObject):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        sprite.Sprite.__init__(self)
        self.image = Surface((WALL_WIDTH, WALL_HEIGHT))
        self.image.fill(Color(WALL_COLOR))
        self.rect = Rect(x,y, WALL_WIDTH, WALL_HEIGHT)


