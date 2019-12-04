RANGE = (138307, 654504)

counter = 0

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
    
print(counter)