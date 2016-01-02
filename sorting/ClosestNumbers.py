__author__ = 'abdujabbor'

n = int(input())
arr = sorted([int(x) for x in input().split()])

_min = 10 ** 14
for x in range(len(arr) - 1, 1, -1):
    _min = min(arr[x] - arr[x - 1], _min)

for x in range(1, len(arr)):
    if arr[x] - arr[x - 1] == _min:
        print(str(arr[x - 1]) + ' ' + str(arr[x]), end=' ')

