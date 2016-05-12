__author__ = 'abdujabbor'

n, m = [int(x) for x in input().split()]
a = [[0] * n] * m
for i in range(n):
    a[i] = [int(x) for x in input().split()]
arr = []
# for i in range(1, len(a) - 1):
#     for j in range(1, a[0] - 1):
#         if a[i][j] != a[i - 1][j] and a[i + 1][j] != a[i][j] and a[i][j] != a[i][j - 1] and a[i][j] != a[i][j + 1]:
#            arr.append(1)
#         else:
#             pass
