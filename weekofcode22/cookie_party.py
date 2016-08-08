__author__ = 'abdujabbor'


n, m = [int(x) for x in input().split()]
if m <= 1:
    print(n - m)
elif m % n == 0:
    print(0)
else:
    c = 0
    if n > m:
        if n % m == 0:
            c = n - m
        else:
            while n % m:
                c += 1
                m += 1
    else:
        t = m // n
        c = (t + 1) * n - m
    print(c)
