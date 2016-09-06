__author__ = 'abdujabbor'

n, k = [int(x) for x in input().split()]

ar = [int(x) for x in input().split()]

charged = int(input())

_s = sum(ar) - ar[k]

_spl = _s // 2


if charged > _spl:
    print(charged - _spl)
else:
    print("Bon Appetit")