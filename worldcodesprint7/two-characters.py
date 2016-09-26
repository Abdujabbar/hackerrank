import operator


def check_string(s):
    if len(s) < 2:
        return False
    ss = list(s)
    x = ss[0]
    y = ss[1]
    if x == y:
        return False

    for x in range(1, len(ss)):
        if ss[x] == ss[x - 1]:
            return False
    return True


n = int(input())
s = input()


_dict = dict()

for x in s:
    if x not in _dict.keys():
        _dict[x] = 1
    else:
        _dict[x] += 1

_sorted_dict = sorted(_dict.items(), key=operator.itemgetter(1))
_max = 0
for x in range(1, len(_sorted_dict)):
    k1 = _sorted_dict[x][0]
    k2 = _sorted_dict[x - 1][0]
    v1 = _sorted_dict[x][1]
    v2 = _sorted_dict[x - 1][1]
    r = ""
    if abs(v1 - v2) <= 1:
        access = [k1, k2]
        for xx in s:
            if xx in access:
                r += xx
        if check_string(r):
            _max = max(_max, len(r))

print(_max)
