__author__ = 'abdujabbor'


n = int(input())
a = [int(x) for x in input().split()]
i = 0
c = 0

while i < n - 1:
    if i + 2 < n and a[i + 2] == 0:
        i += 2
    elif a[i + 1] == 0:
        i += 1
    c += 1
print(c)
