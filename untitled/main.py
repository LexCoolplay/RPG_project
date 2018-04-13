from controls import Controller
from char import Charapter
from Equipment import Equipment
w=Equipment('testarmor','Inhand',0,0)
print(w.call_brief())

controls=Controller()
controls.start()
