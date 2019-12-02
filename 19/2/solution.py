def run(intcode, noun, verb):
	intcode = list(intcode)
	intcode[1] = noun
	intcode[2] = verb
	ip = 0
	while intcode[ip] != 99:
		opcode, a, b, dest = intcode[ip:ip+4]
		a = intcode[a]
		b = intcode[b]
		ip+=4
		if opcode == 1:
			intcode[dest] = a + b
		elif opcode == 2:
			intcode[dest] = a * b
		else:
			print('Invalid opcode:', opcode)
	return intcode[0]

with open('input.txt') as f:
	INPUT = [int(i) for i in f.read().strip('\n').split(',')]

# Part 1
print('1)', run(INPUT, 12, 2))

# Part 2
for noun in range(100):
	for verb in range(100):
		if run(INPUT, noun, verb) == 19690720:
			print('2)', (100 * noun + verb))
			break
