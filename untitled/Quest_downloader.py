from quests import Quest
class Quest_downloader:
    def __init__(self, name):
        self.name = name
        self.dic = {}

    def load(self):
        FILE = open(self.name, 'r');
        for line in FILE:
            x=line.split()
            self.dic[x[1]]=Quest(x[0],x[1])
        return self.dic

    def clear(self):
        self.dic.clear()

    def save(self, dic2):
        self.dic = dic2
        FILE = open(self.name, 'w');
        for i in self.dic:
            FILE.write(self.dic[i].call_brief_data() + '\n')
