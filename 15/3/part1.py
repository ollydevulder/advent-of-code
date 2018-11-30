with open("./input.txt",'r') as input:
    x,y=0,0
    houseArr = [[x,y]]
    visited = 1
    for char in input.readline():
        if char == '<':
            x-=1
        elif char=='>':
            x+=1
        elif char=='^':
            y+=1
        elif char=='v':
            y-=1
        if not [x,y] in houseArr:
            houseArr.append([x,y])
            visited+=1
    print(visited)
