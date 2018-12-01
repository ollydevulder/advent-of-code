with open("input.txt") as input:
    lines = [int(i.strip('\n')) for i in input.readlines()]
    currentFreq = 0
    previousFreqs = [currentFreq]
    foundDupe = False
    while not foundDupe:
        for change in lines:
            result = currentFreq + change
            if result in previousFreqs:
                foundDupe = True
                break
            previousFreqs.append(result)
            currentFreq = result
        print("restarting")
print(result)
