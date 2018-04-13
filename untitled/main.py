import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        super().__init__()
        self.rect = pygame.Rect(start_pos[0], start_pos[1], 20, 20)
        self.climbing = False
    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color('blue'), self.rect)

    def update(self, platforms, movement, ladders):
        for ladder in ladders:
            if pygame.sprite.collide_rect(self, ladder):
                self.climbing = True
        if not self.climbing:
            self.rect.y += 5
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform):
                self.rect.bottom = platform.rect.top
        if movement[0] == 1:
            self.rect.x += 10
        if movement[0] == -1:
            self.rect.x -= 10
        if self.climbing:
            if movement[1] == 1:
                self.rect.y += 10
            if movement[1] == -1:
                self.rect.y -= 10
        self.climbing = False

class Block(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.rect = pygame.Rect(pos[0], pos[1], 50, 10)

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color('gray'), self.rect)


class Ladder(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.rect = pygame.Rect(pos[0], pos[1], 10, 50)

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color('red'), self.rect)


gamecycle = True
pygame.init()


movement = [0, 0]
platforms = []
ladders = []
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
ctrl_pressed = False
hero = None

while gamecycle:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONDOWN:
            if ctrl_pressed and e.button == 1:
                ladders.append(Ladder(e.pos))
            elif e.button == 1:
                hero = Character(e.pos)
            if e.button == 3:
                platforms.append(Block(e.pos))
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                movement[0] = -1
            if e.key == pygame.K_RIGHT:
                movement[0] = 1
            if e.key == pygame.K_UP:
                movement[1] = -1
            if e.key == pygame.K_DOWN:
                movement[1] = 1
            if e.key == pygame.K_LCTRL:
                ctrl_pressed = True
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LCTRL:
                ctrl_pressed = False
        if e.type == pygame.QUIT:
            gamecycle = False

    screen.fill(pygame.Color('black'))
    if hero:
        hero.update(platforms, movement, ladders)
        hero.draw(screen)
    for platform in platforms:
        platform.draw(screen)
    for ladder in ladders:
        ladder.draw(screen)
    pygame.display.flip()
    movement = [0, 0]
pygame.quit()