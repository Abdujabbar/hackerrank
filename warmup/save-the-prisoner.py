

t = int(input())

n, m, s = [int(x) for x in input().split()]


if m == 1:
    print(s)
else:
    if m > n:
        d = m // n
        m -= d * n

    s += m

    if s - 1 > n:
        s -= n
    print(s - 1)
