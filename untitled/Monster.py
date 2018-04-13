from data_downloader_weapons import weapon_downloader
import copy
class Monster:
    def __init__(self, name,level, HP, damage):
        self.HP=HP*(1+level/100)
        self.damage=damage*(1+level/100)
        self.level = int(level)
        self.name = name

    def call_level(self):
        return self.level




    def call_info(self):
        x = "Monster "+str(self.name)+' '+str(self.level)+'LVL'
        return x
    def copy(self):
        return copy.deepcopy(self)

    def call_brief_data(self):
        x = self.name+' '+str(self.level)+'LVL'
        return ' '.join(x)
    def generate_monster(self,level):
        f=False
        self.Hero=self.copy()
        if(self.level>=level*3 and f==False):
            self.Hero.name="Miserable "+self.Hero.name
            f=True
        elif(self.level>=level*2 and f==False):
            self.Hero.name="Weak "+self.Hero.name
            f=True
        elif(level*2>self.level>level*0.5 and f==False):
            f=True
        elif(self.level<level*0.5 and f==False):
            self.Hero.name="Strong "+self.Hero.name
            f=True
        elif(self.level<level*0.33 and f==False):
            self.Hero.name="Dreadful "+self.Hero.name
            f=True
        self.Hero.level=level
        self.Hero.name=self.Hero.name.capitalize()
        return self.Hero


