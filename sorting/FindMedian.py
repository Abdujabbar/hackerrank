__author__ = 'abdujabbor'


def find_median(arr):
    arr = sorted(arr)

    return round((arr[int(len(arr)/2) + 1] + arr[int(len(arr)/2) - 1]) / 2)

n = int(input())
a = [int(x) for x in input().split()]

print(find_median(a))
