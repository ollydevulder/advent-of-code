def hasVowels(string): # check for 3 vowels
    c = 0
    for l in string:
        if l in ['a','e','i','o','u']:
            c+=1
    return c>=3
def hasRep(string): # check for at least 1 case of a repeating character
    for i in range(len(string)):
        if i != 0 and string[i]==string[i-1]:
            return True
    return False
def noBad(string): # check for the bad substrings
    for i in range(len(string)):
        if i!=0 and string[i-2:i] in ['ab', 'cd', 'pq', 'xy']:
            return False
    return True
with open("input.txt",'r') as input:
    words = [line.strip('\n') for line in input]
    totalgood = [word for word in words if hasVowels(word) and hasRep(word) and noBad(word)]
print(len(totalgood))
