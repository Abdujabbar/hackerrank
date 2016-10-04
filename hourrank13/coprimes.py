import math
n = int(input())

def func(x):
    res = 0
    global n
    if (x == 1):
        return 0

    for j in range(2, x):
        if coprime(x / j, x) and x * j == n:
            res += 1

    return res


def coprime(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b
    return a == 1


c = 0
for i in range(n + 1):
    c += func(i)

print(c)