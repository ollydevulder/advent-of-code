with open("input.txt") as input:
    lines = [int(i.strip('\n')) for i in input.readlines()]
    frequency = 0
    for move in lines:
        frequency+=move
    print(frequency)
