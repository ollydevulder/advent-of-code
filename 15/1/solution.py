with open("input.txt", 'r') as input:
    floor, position, counter = 0,0,1
    for char in input.readline():
        if char == '(':
            floor+=1
        elif char == ')':
            floor-=1
        if position==0 and floor == -1:
            position = counter
        counter+=1
    print(floor, position)
