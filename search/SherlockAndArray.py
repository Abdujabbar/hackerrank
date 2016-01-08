__author__ = 'abdujabbor'


for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    found = False
    _sum = sum(a)
    __sum = 0
    for i in range(1, len(a) - 1):
        __sum += a[i - 1]
        d = _sum - __sum - a[i]
        if d == __sum:
            found = True
    if found or len(a) == 1:
        print("YES")
    else:
        print("NO")
