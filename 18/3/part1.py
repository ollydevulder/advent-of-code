with open("input.txt") as input:
    raw_claims = [line.strip('\n').split(" ") for line in input.readlines()]
    claims = {}
    for claim in raw_claims:
        claims[claim[0]] = [[int(c) for c in claim[2].strip(':').split(',')], [int(c) for c in claim[3].split('x')]]
square_inches = [[False for y in range(1000)] for x in range(1000)]
count = 0
for claim in claims:
    Claim = claims[claim]
    for y in range(Claim[0][1], Claim[0][1] + Claim[1][1]):
        for x in range(Claim[0][0], Claim[0][0] + Claim[1][0]):
            sq = square_inches[x][y]
            if sq == None: continue
            elif sq == False: square_inches[x][y] = True
            else:
                count+=1
                square_inches[x][y] = None
print(str(count))
