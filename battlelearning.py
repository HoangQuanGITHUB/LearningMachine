import rps, json
from random import randint
print("You can't win a battle against me >:)")

klf=open('moves.json','r')
movesf=klf.read()
move=json.loads(movesf)['moves']

while True:
    uinput=input('')
    if uinput=='rock':
        uinput=1
    if uinput=='paper':
        uinput=2
    if uinput=='scissors':
        uinput=3
    if uinput=='quit':
        quit()
    else:
        rps.play(uinput,randint(1,3))