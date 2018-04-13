from Monster import Monster
class Monster_downloader:
    def __init__(self, name):
        self.name = name
        self.dic = {}

    def load(self):
        FILE = open(self.name, 'r');
        for string in FILE:
            x = string.split()
            monster_name=x[0]
            level= int(x[1])
            self.dic[monster_name] = Monster(monster_name,level,int(x[2]),int(x[3]))
        return self.dic

    def clear(self):
        self.dic.clear()

    def save(self, dic2):
        self.dic = dic2
        FILE = open(self.name, 'w');
        for i in self.dic:
            FILE.write(self.dic[i].call_brief_data() + '\n')
