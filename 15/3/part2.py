with open("./input.txt",'r') as input:
    x,y=0,0
    x1,y1=0,0
    houseSet = set()
    pos = 1
    for char in input.readline():
        turn = pos%2==0
        if char == '<':
            if turn:
                x-=1
            else:
                x1-=1
        elif char=='>':
            if turn:
                x+=1
            else:
                x1+=1
        elif char=='^':
            if turn:
                y+=1
            else:
                y1+=1
        elif char=='v':
            if turn:
                y-=1
            else:
                y1-=1
        houseSet.add((x,y))
        houseSet.add((x1,y1))
        pos+=1
    print(len(houseSet))
