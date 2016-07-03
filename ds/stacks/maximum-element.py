

s = []
maxs = []
n = int(input())
_max = 0
for x in range(n):
    values = input().split()
    if int(values[0]) == 1:
        if int(values[1]) > _max:
            _max = int(values[1])
            maxs.append(_max)
        s.append(int(values[1]))
        pass
    elif int(values[0]) == 2:
        r = s.pop()
        if len(s) == 0:
            _max = 0
        else:
            if r == _max and len(maxs):
                maxs.pop()
                if len(maxs):
                    _max = maxs.pop()
                else:
                    _max = max(s)

    else:
        print(_max)
        pass

