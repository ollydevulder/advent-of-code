with open("./input.txt") as input:
    dimensions = [sorted([int(n) for n in line.split('x')]) for line in [string.strip('\n') for string in input.readlines()]]
    totalArea, totalBow = 0, 0
    for dms in dimensions:
        l,w,h = dms[0:]
        area = 2*l*w + 2*w*h + 2*h*l + (l*w)
        bowLength = 2*l + 2*w + l*w*h
        totalArea += area
        totalBow += bowLength
    print(totalArea, totalBow)
