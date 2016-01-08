__author__ = 'abdujabbor'


t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    c = 0
    dict_ = dict()
    for i in range(len(a)):
        if a[i] in dict_.keys():
            dict_[a[i]] += 1
        else:
            dict_[a[i]] = 1

    for k, v in dict_.items():
        c += v * (v - 1)
    print(c)
