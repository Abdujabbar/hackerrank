__author__ = 'abdujabbor'


for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    _max = 0
    for i in range(len(a)):
        r = sum(a[len(a) - i - 1:])
        print(r)
        # _max = max(r % m, _max)
    print(_max)
