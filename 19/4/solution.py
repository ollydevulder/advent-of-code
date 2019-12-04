RANGE = (138307, 654504)

counter = 0
counter2 = 0

for i in range(*RANGE):
    s = str(i)
    hasDouble = False
    decreases = True
    prev = s[0]
    for c in s[1:]:
        if prev == c:
            hasDouble = True
        if int(prev) > int(c):
            decreases = False
        prev = c
    if hasDouble and decreases: counter +=1
    if decreases and (s[0] == s[1] != s[2] or s[0] != s[1] == s[2] != s[3] or s[1] != s[2] == s[3] != s[4] or s[2] != s[3] == s[4] != s[5] or s[3] != s[4] == s[5]) : counter2+=1
    
print('1)', counter)
print('2)', counter2)
