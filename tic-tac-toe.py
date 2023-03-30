import random
dic={'t-l':' ','t-m':' ','t-r':' ','m-l':' ','m-m':' ','m-r':' ','d-l':' ','d-m':' ','d-r':' '}
def printbrd(brd):
    print(brd['t-l']+'|'+brd['t-m']+'|'+brd['t-r'])
    print('-+-+-')
    print(brd['m-l']+'|'+brd['m-m']+'|'+brd['m-r'])
    print('-+-+-')
    print(brd['d-l']+'|'+brd['d-m']+'|'+brd['d-r'])
print("enter player names")
name1=input()
name2=input()
print("tossing")
t=['x','o']
turn=random.choice(t)
name=random.choice([name1,name2])
if name==name1:
    anname=name2
else:
    anname=name1
count=9
while count:
    printbrd(dic)
    print("now turn for "+turn +" that is "+name+" where u want to place(exit to terminate)")
    move=input()
    if move=="exit":
        exit()
    if move in dic:
        dic[move] = turn
        count=count-1
    else:
        print("invalid input")
        continue
    if turn=='x':
        temp=name
        name=anname
        anname=temp
        turn='o'
    else:
        turn='x'
        temp=name
        name=anname
        anname=temp
printbrd(dic)
print("Done")

