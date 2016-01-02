def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def reverse(arr, i, j):
    temp = arr[i:j]
    temp = temp[::-1]
    for x in range(len(temp)):
        arr[x + i] = temp[x]


n = int(input())
a = [int(x) for x in input().split()]
_a = a.copy()
_swap = 0
_reverse = 0
x = y = 0

i = 1


if _swap > 0:
    if _swap == 1:
        print("yes")
        print("swap " + str(x + 1) + " " + str(y + 1))
    else:
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                _point = i
                while _point < len(a) and a[_point] < a[_point - 1]:
                    _point += 1
                a[i - 1:_point] = reversed(a[i - 1:_point])
                if is_sorted(a):
                    print("yes")
                    print("reverse" + " " + str(i) + " " + str(_point))
                    _reverse += 1
                break
        if _reverse == 0:
            print("no")
