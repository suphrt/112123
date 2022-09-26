def f(x, q):
    a = []  # a = ''
    while x > 0:
        a.append(x % q)  # a += str(x%q)
        x //= q
        return a[::-1]


s = open('17-345.txt')
a = [int(x) for x in s]
b = [x for x in s if x % 100 == 52]
print(b)

m = max(b) - min(b)
ans = []
for x in range(len(a) - 1):
    if (a[i] < m and a[i + 1] >= m) or (a[i] >= m and a[i + 1] < m):
        ans += [a[i] + a[i + 1]]
print(len(ans), max(ans))
