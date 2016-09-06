
n = int(input())
a = [int(x) for x in input().split()]


m = []

for x in range(len(a)):
    if a[x] == -1:
        m.append(x - a[x])

if m:

    r = 1
    for x in range(len(m)):
        r *= m[x]
    print(r)
else:
    print(1)

