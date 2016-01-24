__author__ = 'abdujabbor'


n = int(input())
an = [int(x) for x in input().split()]
m = int(input())
am = [int(x) for x in input().split()]
_dict_an = dict()
_dict_am = dict()
for i in range(len(an)):
    if an[i] in _dict_an.keys():
        _dict_an[an[i]] += 1
    else:
        _dict_an[an[i]] = 1
for i in range(len(am)):
    if am[i] in _dict_am.keys():
        _dict_am[am[i]] += 1
    else:
        _dict_am[am[i]] = 1


# print(sorted(_dict_an))

for i in sorted(_dict_an):
    if _dict_an[i] != _dict_am[i]:
        print(i, end=' ')
