with open('input.txt') as f:
	raw = f.read().strip('\n')
INPUT = [int(r) for r in raw.split('\n')]

mass1 = sum([i//3-2 for i in INPUT])
print(f'1) {mass1}')

def get_mass(n): # ooo recursion
	new = n//3-2
	if new <= 0:
		return 0
	return new + get_mass(new)

reqs = [get_mass(i) for i in INPUT]
mass2 = sum(reqs)
print(f'2) {mass2}')
