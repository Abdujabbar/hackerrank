def array_left_rotation(a, n, k):
    return a[k:] + a[:k]

n, k = map(int, input().strip().split(' '))
a = [int(x) for x in input().split()]
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')
