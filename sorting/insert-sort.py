__author__ = 'abdujabbor'


def inversions(arr):
    n = len(arr)
    if n == 1:
        return 0
    n1 = int(n/2)
    n2 = int(n - n1)
    arr1 = arr[:n1]
    arr2 = arr[n1:]
    ans = inversions(arr1) + inversions(arr2)
    i1 = 0
    i2 = 0
    for i in range(n):
        if i1 < n1 and (i2 >= n2 or arr1[i1] <= arr2[i2]):
            arr[i] = arr1[i1]
            ans += i2
            i1 += 1
        elif i2 < n2:
            arr[i] = arr2[i2]
            i2 += 1
    return ans


n = int(input())
for _ in range(n):
    s = int(input())
    a = [int(x) for x in input().split()]
    print(inversions(a))
