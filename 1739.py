def f(x, q):
    a = [] # a = ''
    while x > 0:
        a.append(x%q) # a += str(x%q)
        x //= q
        return a[::-1]
a = []
for x in range(3466, 9081+1):
    if (len(f(x, 8)) != len(f(x, 10))) and (x%7 ==1 or x&7 == 5):
        a.append(x)
print(len(a), max(a))
