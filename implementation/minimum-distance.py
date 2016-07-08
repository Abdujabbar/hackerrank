
n = int(input())
a = [int(x) for x in input().split()]


if n > 1:
    sa = sorted(a)
    paired = []
    for x in range(len(sa) - 1):
        if sa[x] != sa[x + 1]:
            continue
        else:
            paired.append(sa[x])
            x += 1
    _min = 10 ** 5 + 1
    for x in range(len(a)):
        if a[x] not in paired:
            continue
        else:
            ll = len(a) - 1
            if ll != x:
                f = False
                while ll > x:
                    if a[ll] == a[x]:
                        f = True
                        break
                    ll -= 1
                if f:
                    _min = min(_min, abs(ll - x))
    if _min == 10 ** 5 + 1:
        print(-1)
    else:
        print(_min)
else:
    print(-1)




