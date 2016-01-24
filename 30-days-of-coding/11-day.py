__author__ = 'abdujabbor'


a = [None]*6

for i in range(6):
    a[i] = [int(x) for x in input().split()]


_sum = -9 * 7
for i in range(len(a) - 2):

    for j in range(len(a[0]) - 2):
        __sum = 0
        for t in range(j, j + 3):
            __sum += a[i][t] + a[i + 2][t]
        __sum += a[i + 1][j + 1]
        if __sum > _sum:
            _sum = __sum
print(_sum)