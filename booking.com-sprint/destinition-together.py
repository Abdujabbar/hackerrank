__author__ = 'abdujabbor'

n, m, c = [int(x) for x in input().split()]

k = n - c + m - c + c

r = 1

for x in range(1, k):
    r *= x


print(r)