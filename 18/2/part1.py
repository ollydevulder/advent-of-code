with open("input.txt") as input:
    words = [word.strip('\n') for word in input.readlines()]
twos, threes = 0, 0
for word in words:
    counted2, counted3 = False,False
    for letter in word:
        if word.count(letter) == 2 and not counted2:
            counted2 =True
            twos+=1
        elif word.count(letter) == 3 and not counted3:
            counted3 = True
            threes+=1
checksum = twos*threes
print(checksum)
