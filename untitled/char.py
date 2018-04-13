from data_downloader_weapons import weapon_downloader
from Equipment import Equipment
class Charapter:
    def __init__(self,name="No_charapter",level=1,armor='Chest',weapon1='Fist',weapon2='Fist',magic='Nothing'):
        WEAPONS=weapon_downloader("weapons.txt")
        self.arr=WEAPONS.load()
        self.Armor=self.arr[armor]
        self.Weapon_1=self.arr[weapon1]
        self.Weapon_2=self.arr[weapon2]
        self.level=int(level)
        self.Magic=self.arr[magic]
        self.name=name
        self.HP=100+10*self.level+3*self.Armor.call_level_bonus()
        self.damage=40+3*self.level+3*self.Weapon_2.call_level_bonus()+3*self.Weapon_1.call_level_bonus()
        self.differ=self.Magic.call_level_bonus()
    def call_level(self):
        return self.level
    def call_power(self):
        return (self.Armor.call_level_bonus()+self.Magic.call_level_bonus()+self.Weapon_1.call_level_bonus()+self.Weapon_2.call_level_bonus())
    def call_info(self):
        x="Charapter "+str(self.call_level())+'LVL '+ ':\n'+self.Armor.call_info()+self.Weapon_1.call_info()+self.Weapon_2.call_info()+self.Magic.call_info()
        return x
    def call_brief_data(self):
        x=[self.name,str(self.level),str(self.Armor.name),str(self.Weapon_1.name),str(self.Weapon_2.name),str(self.Magic.name)]
        return ' '.join(x)