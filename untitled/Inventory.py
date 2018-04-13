class Item:
    def __init__(self,image, name):
        self.image = image
        self.name = name
        self.rect = self.image.get_rect()

    def set_position(self, x, y):
        self.rect.x, self.rect.y = x, y

    def draw(self,screen, into_rect= None):
        screen.blit(self, self.rect, into_rect)


class Weapon(Item):
    def __init__(self,image, name, damage):
        super().__init__(image,name)
        self.damage = damage
    def get_damage(self):
        return self.damage
class Consumable(Item):
    def __init__(self, image, name, script):
        super().__init__(image, name)
        self.script = script
        self.type = 'consumable'
    def get_script(self):
        return self.script


