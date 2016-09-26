n, m, k = [int(x) for x in input().split()]

c = 0
for i in range(k):
    r, c1, c2 = [int(x) for x in input().split()]
    c += (c2 - (c1 - 1))

print(m * n - c)
