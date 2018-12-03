from sys import stdout
with open("input.txt") as input:
    raw_claims = [line.strip('\n').split(" ") for line in input.readlines()]
    claims = {}
    for claim in raw_claims:
        claims[claim[0]] = [[int(c) for c in claim[2].strip(':').split(',')], [int(c) for c in claim[3].split('x')]]
square_inches = []
visited = []
count = 0
raw_claims = None
print("Overlaps found:\n")
for claim in claims:
    this_claim = claims[claim]
    for y in range(this_claim[1][1]):
        y+=this_claim[0][1]
        for x in range(this_claim[1][0]):
            x+=this_claim[0][0]
            if [x, y] in square_inches and [x, y] not in visited:
                count+=1
                visited.append([x, y])
                stdout.write("\r"+str(count))
                stdout.flush()
            square_inches.append([x,y])
print("\n"+str(count))
