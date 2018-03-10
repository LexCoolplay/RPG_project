class Item:
    def __init__(self,image, name):
        self.image = image
        self.name = name
    def draw(self,screen,into_rect):
        screen.blit(self, (0,0), into_rect)
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
    def get_script(self):
        return self.script


