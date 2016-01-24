__author__ = 'abdujabbor'


n, m = [int(x) for x in input().split()]
a = [[0]*m]*n
p = [0] * n
for i in range(n):
    a[i] = sorted([int(x) for x in input().split()])
    p[i] = min(a[i])


print(max(p))
