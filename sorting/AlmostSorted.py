def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def reverse(arr, i, j):
    t = arr[i:j + 1]
    arr[i:j+1] = reversed(t)


n = int(input())
a = [int(x) for x in input().split()]

if is_sorted(a):
    print("yes")
else:
    sorted_a = sorted(a)

    i = 0
    j = len(a) - 1
    while i < j - 1 and a[i] < a[i + 1]:
        i += 1

    while j > 0 and a[j] > a[j - 1]:
        j -= 1

    _a = a.copy()
    swap(_a, i, j)
    if is_sorted(_a):
        print("yes")
        print("swap " + str(i + 1) + " " + str(j + 1))
    else:
        reverse(a, i, j)
        if is_sorted(a):
            print("yes")
            print("reverse " + str(i + 1) + " " + str(j + 1))
        else:
            print("no")

