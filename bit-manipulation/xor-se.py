
t = int(input())

for _ in range(t):
    a, b = [int(x) for x in input().split()]

    r = a
    while r % 4 != 0:
        r -= 1

    k = r
    res = None
    while r <= b:

        if r >= a:
            if res:
                res = res ^ k
            else:
                res = k
        r += 1
        k = k ^ r
    print(res)
