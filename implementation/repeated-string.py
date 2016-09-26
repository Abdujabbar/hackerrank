s = input()
n = int(input())
c = s.count('a')
if n % len(s) == 0:
    print((n // len(s)) * c)
else:
    _len = len(s)
    _n = n
    while _n % _len != 0:
        _n -= 1

    r = (n // _len) * c
    sl = list(s)
    r += "".join(sl[:n - _n]).count('a')
    print(r)
