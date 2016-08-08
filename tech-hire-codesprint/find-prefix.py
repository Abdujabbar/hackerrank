__author__ = 'abdujabbor'

t = int(input())

for _ in range(t):
    n = int(input())
    ar = []
    for __ in range(n):
        ar.append(input())
    ar = sorted(ar)
    _max = 0
    for x in range(1, len(ar)):
        s1 = ar[x]
        s2 = ar[x - 1]
        p = 0
        q = 0
        while p < len(s1) and q < len(s2) and s1[p] == s2[q]:
            q += 1
            p += 1
        _max = max(_max, p)
    print(_max)