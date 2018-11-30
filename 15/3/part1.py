class house:
    def __init__(self,x,y):
        self.x,self.y = x,y
def checkForHouse(arr,x,y):
    for i in arr:
        if i.x == x and i.y == y:
            return True
    return False
with open("./input.txt",'r') as input:
    x,y=0,0
    houseArr = [house(0,0)]
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
        if not checkForHouse(houseArr,x,y):
            houseArr.append(house(x,y))
            visited+=1
    print(visited)
