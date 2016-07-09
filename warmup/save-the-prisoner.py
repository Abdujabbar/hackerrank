
t = int(input())

for _ in range(t):
    n, m, s = [int(x) for x in input().split()]

    if m == 1:
        print(s)
    else:
        if m > n:
            d = m // n
            m -= d * n

        s += m - 1

        if s > n:
            s -= n
        print(s)

