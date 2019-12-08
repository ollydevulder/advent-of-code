width = 25
height = 6

with open('input') as f:
	data = f.read().strip('\n')

layers = [data[i:i+(width*height)] for i in range(0, len(data), height*width)]
fewest_0 = min(layers, key=lambda x: x.count('0'))

# Part 1
print('1)', fewest_0.count('1') * fewest_0.count('2'))

# Part 2

print('2)')
decoded = ''
for i in range(width * height):
	for l in layers:
		state = l[i]
		if state == '2':
			continue
		else:
			decoded += state
			break

for i in range(0, len(decoded), width):
	print(decoded[i:i+width+1].replace('1','█').replace('0', ' '))
