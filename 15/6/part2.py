import sys
lights = [[0 for j in range(1000)] for i in range(1000)]
def total_brightness():
    total=0
    for row in lights:
        for light in row:
            total+=light
    return total
def change(mode, x,y, x1,y1):
    for i in range(1000):
        for j in range(1000):
            if j>=x and j<=x1 and i>=y and i<=y1:
                if mode == 'toggle':
                    lights[i][j] += 2
                elif mode == 'on':
                    lights[i][j] += 1
                elif mode == 'off' and lights[i][j] > 0:
                    lights[i][j] -= 1
with open("input.txt") as input:
    instructions = [line.split(' ') for line in input.readlines()]
    for i in instructions:
        sys.stdout.write("\r{} bright".format(total_brightness()))
        sys.stdout.flush()
        mode = i[0]
        if mode == "turn":
            mode = i[1]
            del i[0]
        del i[2]
        i[2] = i[2].strip('\n')
        i[1],i[2] = [int(a) for a in i[1].split(',')], [int(a) for a in i[2].split(',')]
        change(i[0],i[1][0],i[1][1],i[2][0],i[2][1])
print('\n{}'.format(total_brightness()))
