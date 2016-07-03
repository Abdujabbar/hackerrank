__author__ = 'abdujabbor'

a, b = [int(x) for x in input().split()]

ar = [int(x) for x in input().split()]

# r = []
for x in range(len(ar)):
    v = ar[x + b - len(ar)]
    # r.append(v)
    print(v, end=' ')

