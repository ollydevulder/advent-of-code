with open("./input.txt",'r') as input:
    x,y=0,0
    houseSet = set()
    for char in input.readline():
        if char == '<':
            x-=1
        elif char=='>':
            x+=1
        elif char=='^':
            y+=1
        elif char=='v':
            y-=1
        houseSet.add((x,y))
    print(len(houseSet))
