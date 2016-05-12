
def check(m, v):
    if len(m) == 0:
        m.append(v)
        return
    vv = m.pop()
    if v >= vv:
        m.append(vv)
        m.append(v)
    else:
        m.append(v)
        m.append(vv)

t = int(input())

_list = []
_max = []
for _ in range(t):
    command = input().split()
    c = int(command[0])

    if c == 1:
        x = int(command[1])
        _list.append(x)
        check(_max, x)
    elif c == 2:
        v = _list.pop()
        _max.remove(v)
    elif c == 3:
        print(_max[len(_max) - 1])
