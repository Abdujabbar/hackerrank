

n = int(input())

a = sorted([int(x) for x in input().split()])

_sum = sum(a) // 2
c = 0
for x in range(len(a)):
    if a[x] >= _sum:
        c += 1

print(c)