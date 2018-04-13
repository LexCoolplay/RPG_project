from Equipment import Equipment
class weapon_downloader:
    def __init__(self, name):
        self.name = name
        self.arr=dict()

    def load(self):
        FILE = open(self.name, 'r');
        for string in FILE:
            x=string.split()
            self.arr[x[0]]=Equipment(str(x[0]),str(x[1]),int(x[2]),int(x[3]))
        return self.arr

    def clear(self):
        self.arr=[]

    def save(self,arr2):
        self.arr=arr2
        FILE = open(self.name, 'w');
        for i in self.arr:
            FILE.write(self.arr[i].call_brief() + '\n')
