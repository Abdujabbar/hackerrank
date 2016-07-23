__author__ = 'abdujabbor'

n = int(input())

for _ in range(n):
    s = input()
    r = set()
    for x in s:
        r.add(x)

    print(len(r))
