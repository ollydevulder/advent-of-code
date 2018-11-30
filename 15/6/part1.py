import sys
lights = [[False for j in range(1000)] for i in range(1000)]
def totalOn():
    count=0
    for row in lights:
        for light in row:
            if light:
                count+=1
    return count
def change(mode, x,y, x1,y1):
    for i in range(1000):
        for j in range(1000):
            if j>=x and j<=x1 and i>=y and i<=y1:
                if mode == 'toggle':
                    lights[i][j] = not lights[i][j]
                elif mode == 'on':
                    lights[i][j] = True
                elif mode == 'off':
                    lights[i][j] = False
with open("input.txt") as input:
    instructions = [line.split(' ') for line in input.readlines()]
    counter = 0
    total = len(instructions)
    for i in instructions:
        sys.stdout.write("\r{}%".format(round(counter/total * 100, 1)))
        sys.stdout.flush()
        mode = i[0]
        if mode == "turn":
            mode = i[1]
            del i[0]
        del i[2]
        i[2] = i[2].strip('\n')
        i[1],i[2] = [int(a) for a in i[1].split(',')], [int(a) for a in i[2].split(',')]
        change(i[0],i[1][0],i[1][1],i[2][0],i[2][1])
        counter+=1
print(totalOn())
