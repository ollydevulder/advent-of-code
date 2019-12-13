from computer import *
from itertools import permutations

with open('input') as f:
	data = f.read()

highest = 0

for setting in permutations(range(5)):
	print(' '.join([str(i) for i in setting]))
	computer = Computer(data)
	last = 0
	for phase in setting:
		print(phase)
		computer.__init__(data)
		last = computer.run(phase, last)
	if last > highest:
		highest = last

print(highest)
