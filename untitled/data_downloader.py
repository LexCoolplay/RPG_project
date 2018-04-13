from char import Charapter
class data_downloader:
    def __init__(self, name):
        self.name = name
        self.dic = {}

    def load(self):
        FILE = open(self.name, 'r');
        for string in FILE:
            x = string.split()
            charapter_name=x[0]
            level, armor, weapon1, weapon2, magic = str(x[1]),str(x[2]),str(x[3]),str(x[4]),str(x[5])
            self.dic[charapter_name] = Charapter(charapter_name,level,armor,weapon1,weapon2,magic)
        return self.dic

    def clear(self):
        self.dic.clear()

    def save(self, dic2):
        self.dic = dic2
        FILE = open(self.name, 'w');
        for i in self.dic:
            FILE.write(self.dic[i].call_brief_data() + '\n')
