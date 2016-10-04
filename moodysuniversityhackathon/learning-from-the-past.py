__author__ = 'abdujabbor'


n = int(input())
_max = 0
for _ in range(n):
    a, b, c = sorted([int(x) for x in input().split()], reverse=True)
    _max = max(a + b, _max)

print(_max)
