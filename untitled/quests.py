import random
from Loot_generator import Treasure
class Quest:
    def __init__(self,level,name):
        self.level=level
        self.name=name
    def calculate_perfomance(self,char_level):
        differ=50*(int(char_level)/int(self.level))
        result=random.randint(1, 100)
        if(differ>=result):
            return self.calculate_loot()
        else:
            return self.calculate_loss()
    def calculate_loot(self):
        loot=Treasure()
        result=random.randint(1,100)
        if(result<20):
            return True
        elif(result<94):
            return random.choice(loot.get_pool(int(self.level)))
        else:
            return random.choice(loot.get_pool(int(self.level)+5))
    def calculate_loss(self):
        return False
    def call_info(self):
        x="Quest in "+self.name+'. Recomended level: '+self.level+'.'
        return x
    def call_brief_data(self):
        x=self.level+' '+self.name

