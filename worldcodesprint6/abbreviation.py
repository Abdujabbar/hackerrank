__author__ = 'abdujabbor'


def makeable(a, b):
    if len(a) < len(b):
        return False

    aa = ''
    for x in a:
        if 'A' <= x <= 'Z' and x not in b:
            return False
        if 'a' <= x <= 'z' and x.upper() not in b:
            continue

        aa += x

    if len(aa) < len(b):
        return False

    aa = sorted(list(aa))
    bb = sorted(b)

    while aa and 'A' <= aa[0] <= 'Z' and bb:
        atop = aa[0]
        if atop in bb:
            bb.remove(atop)
            aa.pop(0)
        else:
            break

    if len(bb) == 0:
        while aa:
            atop = aa.pop()
            if 'A' <= atop <= 'Z':
                return False
        return True
    else:
        while bb:
            btop = bb.pop()
            if btop.lower() not in aa:
                return False
            else:
                try:
                    aa.remove(btop)
                except:
                    aa.remove(btop.lower())

        while aa:
            atop = aa.pop()
            if 'A' <= atop <= 'Z':
                return False

        return True


q = int(input())

for _ in range(q):
    a = input()
    b = input()
    if makeable(a, b):
        print("YES")
    else:
        print("NO")
