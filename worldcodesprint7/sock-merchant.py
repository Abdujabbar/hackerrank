__author__ = 'abdujabbor'

n = int(input())

a = sorted([int(x) for x in input().split()])

pairs = dict()
r = 0
for x in a:
    if x in pairs.keys():
        pairs[x] += 1
    else:
        pairs[x] = 1


for key, item in pairs.items():
    if item & 1:
        r += (item - 1) // 2
    else:
        r += item // 2

print(r)