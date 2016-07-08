n, k = [int(x) for x in input().split()]

a = sorted([int(x) for x in input().split()])

c = 0

if len(a) == 0:
    print(-1)
else:
    v = a.pop(0)
    if len(a) > 1:
        while len(a) >= 1 and v < k:
            v2 = a.pop(0)
            insert = v + 2 * v2
            c += 1
            for x in range(len(a)):
                if insert > a[x]:
                    continue
                else:
                    break
            a.insert(x, insert)
            v = a.pop(0)

        if v >= k:
            print(c)
        else:
            print(-1)
    else:
        if v >= k:
            print(c)
        else:
            print(-1)

