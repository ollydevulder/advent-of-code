wires = {}

def check(wire):
    return type(wire) == int

with open("input.txt",'r') as input:
    lines = [line.strip('\n').split(' ') for line in input.readlines()]

for line in lines:
    wires[line[-1]] = line[:-1]
    del wires[line[-1]][-1]

while not check(wires["a"]):
    for wire in wires:
        print('#',end='')
        if wire[0] == wire[-1]:
            a = wires[wire[0]]
            if check(a):
                wires[wire] = a
        elif wire[0] == "NOT":
            a = wires[wire[1]]
            if check(a):
                wires[wire] = ~ a
        elif wire[1] == "LSHIFT":
            a = wires[wire[0]]
            b = wires[wire[2]]
            if check(a) and check(b):
                wires[wire] = a << b
        elif wire[1] == "RSHIFT":
            a = wires[wire[0]]
            b = wires[wire[2]]
            if check(a) and check(b):
                wires[wire] = a >> b
        elif wire[1] == "OR":
            a = wires[wire[0]]
            b = wires[wire[2]]
            if check(a) and check(b):
                wires[wire] = a | b
print(wires["a"])
