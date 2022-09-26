a = []
for x in range(2461, 9719+1):
    if (3 <= (x//10%10) <= 7 ) and (1 != (x//10%10) and (9 != (x//10%10))):
        a.append(x)
print(len(a), max(a))