def getCoords(path):
    coords = set()
    pos = [0,0]
    for instruction in path:
        d = instruction[0]
        dist = int(instruction[1:])
        x, y = pos
        if d == 'R':
            c = [(i, y) for i in range(x+1, x+dist+1)]
            pos[0] += dist
        elif d == 'L':
            c = [(i, y) for i in range(x-1, x-dist-1, -1)]
            pos[0] -= dist
        elif d == 'U':
            c = [(x, i) for i in range(y+1, y+dist+1)]
            pos[1] += dist
        else:
            c = [(x, i) for i in range(y-1, y-dist-1, -1)]
            pos[1] -= dist
        coords.update(c)
    return coords

with open('input.txt') as f:
    data = f.read()

pathA, pathB = [[i for i in path.split(',')] for path in data.split('\n')]
pointsA, pointsB = getCoords(pathA), getCoords(pathB)
distances = [abs(i[0]) + abs(i[1]) for i in set(pointsA & pointsB)]

print('1)', min(distances))