with open("input.txt") as input:
    words = [word.strip('\n') for word in input.readlines()]
def checkWords(stringA, stringB):
    count = 0
    index = 0
    for i in range(len(stringA)):
        if stringA[i] != stringB[i]:
            count+=1
            index = i
    return count == 1, index
correctBoxA = False
correctBoxB = False
difference  = None
for wordA in words:
    for wordB in words:
        if wordA == wordB:
            break
        diff, difference = checkWords(wordA, wordB)
        if diff:
            correctBoxA = wordA
            correctBoxB = wordB
            break
    if correctBoxA and correctBoxB:
        break
same = correctBoxA[:difference] + correctBoxA[difference+1:]
print(same)
