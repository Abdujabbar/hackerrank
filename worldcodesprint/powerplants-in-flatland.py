__author__ = 'abdujabbor'

n, m = [int(x) for x in input().split()]
lst = [0] * n
zeros = sorted([int(x) for x in input().split()])
lz = len(zeros)
if len(zeros) == n:
    print(0)
else:
    for i in range(lz):
        lst[zeros[i]] = -1
    for i in range(n):
        if lst[i] == -1:
            continue
        else:
            j = 0
            while j < lz - 1 and zeros[j] < i:
                j += 1
            lst[i] = min(abs(i - zeros[j]), (i - zeros[j - 1]))
    print(max(lst))



