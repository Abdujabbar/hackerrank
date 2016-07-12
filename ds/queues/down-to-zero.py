

q = int(input())

for _ in range(q):
    n = int(input())
    c = 0
    q = []
    t = n
    while n != 0:
        f = False
        q = [int(x) for x in range(2, int(n ** 1/2))]

        while q:
            i = q.pop(0)
            if n % i == 0:
                n = max(i, int(n / i))
                c += 1

        n -= 1
        c += 1

    print(c)
