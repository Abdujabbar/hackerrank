import operator
n, m, k = [int(x) for x in input().split()]

_dict = dict()

for _ in range(k):
    r, c1, c2 = [int(x) for x in input().split()]
    if r not in _dict.keys():
        _dict[r] = []
        _dict[r].append({"c1": c1, "c2": c2})
    else:
        _dict[r].append({"c1": c1, "c2": c2})
_ends = dict()
r = 0
for key, lines in _dict.items():
    for item in lines:
        if key not in _ends.keys():
            r += (item['c2'] - item['c1'] + 1)
            _ends[key] = []
            _ends[key].append(item['c2'])
        else:
            __max = _ends[key].pop()
            a1 = item['c1']
            a2 = item['c2']
            if __max > a1:
                a1 = __max
            if a2 > a1:
                r += (a2 - a1)
            _ends[key].append(max(item['c2'], __max))

print(m * n - r)
