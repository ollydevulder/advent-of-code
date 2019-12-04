def getCoords(path, coord=False):
	if not coord:
		coords = set()
	else:
		counter = 0
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
		if not coord:
			coords.update(c)
		else:
			if coord in c:
				counter+=c.index(coord)+1
				return counter
			else:
				counter+=dist
	return coords

with open('input.txt') as f:
    data = f.read()

pathA, pathB = [[i for i in path.split(',')] for path in data.split('\n')]
pointsA, pointsB = getCoords(pathA), getCoords(pathB)
intersection = set(pointsA & pointsB)
min_distance = min([abs(i[0]) + abs(i[1]) for i in intersection])
min_steps    = min([getCoords(pathA, i) + getCoords(pathB, i) for i in intersection])

print('1)', min_distance)
print('2)', min_steps)
