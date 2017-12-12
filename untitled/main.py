from pygame.locals import *
import pygame
import os
from Hero import Hero
from Wall import Wall
from camera import *
from locals import *
left=right=up=down=False
from Enemy import Enemy

GRID=[]
pygame.init()
display=pygame.display
screen = display.set_mode(resolution)
event=pygame.event
bg=pygame.Surface(resolution)

bg.fill(Color("#004400"))
x,y=0,0
clock=pygame.time.Clock()
dic={0:0,1:0,2:0,3:0}
image=pygame.image.load(os.path.join("PlayerTest.png"))
hero=Hero(image,64,64)

enemies=[]
entities = pygame.sprite.Group()
platforms= []
level= [
    "----------------------------------------------------",
    "-                                                  -",
    "-                                                  -",
    "-                                                  -",
    "-                                                  -",
    "-                                                  -",
    "-                                     *            -",
    "-                                                  -",
    "-         -             ------------------         -",
    "-         -             -                          -",
    "-         -             -                          -",
    "-         -             -                          -",
    "-         -             -                          -",
    "-         -             -                          -",
    "-         -             -                          -",
    "-         -             -                          -",
    "-         -             -                          -",
    "-         ---------------------------------        -",
    "-                       -                 -        -",
    "-                       -                 -        -",
    "-                       -                 -        -",
    "-                       -                 -        -",
    "-                       -                 -        -",
    "-                       -                 -        -",
    "-                       -                 -        -",
    "-                       -                 -        -",
    "-                       -                 -        -",
    "-        ----------------                 -        -",
    "-                                                  -",
    "-                                                  -",
    "-                                                  -",
    "-                                                  -",
    "-                                                  -",
    "-                                                  -",
    "-                                                  -",
    "-                                                  -",
    "----------------------------------------------------",
]
entities.add(hero)
left=right=up=down=False

total_level_width = len(level[0]) * WALL_WIDTH  # Высчитываем фактическую ширину уровня
total_level_height = len(level) * WALL_HEIGHT  # высоту

camera = Camera(camera_configure, total_level_width, total_level_height)
x = y = 0;
for row in level:
    for col in row:
        if col == "-":
             pf = Wall(x, y)
             entities.add(pf)
             platforms.append(pf)
        if col == '*':
           en=Enemy(x,y)
           entities.add(en)
           enemies.append(en)
        x += WALL_WIDTH
    y += WALL_HEIGHT
    x = 0;
while game_loop:
    clock.tick(30)

    for i in event.get():
        if i.type == QUIT:
            raise SystemExit
        if i.type == KEYDOWN and i.key == K_UP:
            up=True
        if i.type == KEYDOWN and i.key == K_DOWN:
            down=True
        if i.type == KEYDOWN and i.key == K_LEFT:
            left=True
        if i.type == KEYDOWN and i.key == K_RIGHT:
            right=True
        if i.type == KEYUP and i.key == K_UP:
            up=False
        if i.type == KEYUP and i.key == K_DOWN:
            down=False
        if i.type == KEYUP and i.key == K_LEFT:
            left=False
        if i.type == KEYUP and i.key == K_RIGHT:
            right=False
        #print(i)
    screen.blit(image, (0, 0))
    #screen_layer
    screen.blit(bg, (0, 0))
    #entity_layer
    screen.fill(bgColor)
    hero.update(left, right, up, down,platforms,enemies)
    camera.update(hero)
    for e in entities:
        screen.blit(e.image, camera.apply(e))
    for en in enemies:
        en.update(platforms,hero)
        en.draw(screen)
        if en.dead:
            enemies.remove(en)
            entities.remove(en)
    pygame.display.update()


pygame.quit()

