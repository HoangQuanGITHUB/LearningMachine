def play(uinput:int,cinput:int):
    #1=rock
    #2=paper
    #3=scissors
    if cinput==1:
        c2input='rock'
    if cinput==2:
        c2input='paper'
    if cinput==3:
        c2input='scissors'
    print(c2input)
    if c2input==1 and cinput==2:
        print('Computer wins!')
    if uinput==2 and cinput==3:
        print('Computer wins!')
    if uinput==3 and cinput==1:
        print('Computer wins!')
    if cinput==1 and uinput==2:
        print('User wins!')
    if cinput==2 and uinput==3:
        print('User wins!')
    if cinput==3 and uinput==1:
        print('User wins!')
    if uinput==cinput:
        print('Tie!')