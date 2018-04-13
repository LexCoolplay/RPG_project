from data_downloader import data_downloader
from data_downloader_weapons import weapon_downloader
from char import Charapter
from Equipment import Equipment
from Quest_downloader import Quest_downloader
from Monster_downloader import Monster_downloader
import random
class Game:
    def __init__(self):
        self.dic={}
        self.Hero=Charapter()


    def load_data(self):
        data=data_downloader('data.txt')
        weapons=weapon_downloader('weapons.txt')
        quests=Quest_downloader('quests.txt')
        monsters=Monster_downloader('monsters.txt')
        self.arr=weapons.load()
        self.dic=data.load()
        self.quests=quests.load()
        self.monsters=monsters.load()


    def save_data(self):
        data=data_downloader('data.txt')
        weapons=weapon_downloader('weapons.txt')
        weapons.save(self.arr)
        data.save(self.dic)


    def register(self,name):
        if(name in self.dic.keys()):
            print("This name is already exist!")
        else:
            self.dic[name]=Charapter(name)
            self.save_data()
            print("Success!")


    def fight(self,name1,name2):
        if(name1 in self.dic.keys() and name2 in self.dic.keys()):
            if(self.dic[name1].call_power()>self.dic[name2].call_power()):
                print(name1,'wins!')
            elif(self.dic[name2]>self.dic[name1]):
                print(name2,'wins!')
            else:
                print('Draw!')
        else:
            print("One of the warriors isn't exist!")


    def forge(self,name,type,level_bonus,level):
        weapon=Equipment(name,type,level_bonus,level)
        if(weapon not in self.arr):
            self.arr[weapon.name]=weapon
            self.save_data()
            print("Successfuly added to weapons!")
        return weapon


    def ask_trade(self,weapon):
        print("You find:"+' '+weapon.call_info()+'.')
        x=input('Do you want to pick it up and drop your current weapon? Y/N ')
        if(x[0]=='Y'):
            if(weapon.type=='Armor'):
                self.Hero.Armor=weapon
            elif(weapon.type=='Inhand'):
                x=input('Which hand? L/R')
                if(x[0]=='L'):
                    self.Hero.Weapon_1=weapon
                else:
                    self.Hero.Weapon_2=weapon
            elif(weapon.type=='Magic'):
                self.Hero.Magic=weapon
        else:
            pass


    def log_in(self,name):
        if(name in self.dic.keys()):
            self.Hero=self.dic[name]
            print("Logged in Succesfuly!")
            return True
        else:
            print("No such charapter!")
            return False


    def start_quest(self,name):
        Mission=self.quests[name]
        success=Mission.calculate_perfomance(self.Hero.level)
        if(success==False and self.Hero.level!=1):
            print("Defeat!")
            self.Hero.level-=1
        elif(success==True):
            self.Hero.level+=1
        else:
            print("Victory!")
            self.Hero.level+=1
            self.ask_trade(self.arr[success])

    def summon_monster(self,name,level):
        return self.monsters[name].generate_monster(level)
    def challenge_monster(self,monster):
        fl=random.choice([True,False])
        past_HP_M=monster.HP
        past_HP_H=self.Hero.HP
        while(True):
            if(past_HP_M<=0):
                print("Victory! Monster defeated!")
                return True
            elif(past_HP_H<=0):
                print("Defeat!")
                return False
            elif(fl == True):
                    x=int(int(self.Hero.damage)+random.randint(0,self.Hero.differ))
                    past_HP_M -= x
                    print(self.Hero.name,'slash',monster.name,'with',x,'damage!')
                    print(self.Hero.name+":",past_HP_H)
                    print(monster.name+':',past_HP_M)
                    fl=False
            elif(fl == False):
                    x=monster.damage
                    print(monster.name,'hit',self.Hero.name,'with',x,'damage!')
                    past_HP_H -= x
                    print(self.Hero.name+":",past_HP_H)
                    print(monster.name+':',past_HP_M)

                    fl=True





