__author__ = 'abdujabbor'


a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]


c = 0

for i in range(len(a)):
    if a[i] == b[i]:
        continue
    else:
        if a[i] > b[i]:
            r = b[i] + 10 - a[i]
            c += min(abs(a[i] - b[i]), r)
        else:
            r = a[i] + 10 - b[i]
            c += min(abs(a[i] - b[i]), r)

print(c)
