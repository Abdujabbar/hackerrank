def validate(matrix, i, j, dist):
    global n
    top = i - dist
    bottom = i + dist
    left = j - dist
    right = j + dist
    notvalid = top < 0 or bottom >= n or left < 0 or right >= n

    if notvalid:
        return False

    if matrix[top][j] == matrix[bottom][j] == matrix[i][left] == matrix[i][right] == '.':

        topside = i
        bottomside = i
        cc = 1
        while topside >= top and bottomside <= bottom:
            topside -= 1
            bottomside += 1
            leftside = left + cc
            rightside = right - cc
            while leftside <= rightside:
                if matrix[topside][rightside] != '.' or matrix[topside][leftside] != '.' or\
                        matrix[bottomside][rightside] != '.' or matrix[bottomside][leftside] != '.':
                    return False
                leftside += 1
                rightside -= 1
            cc += 1
        return True

    return False


def distance(matrix, i, j):
    _max = 0
    c = 1
    while validate(matrix, i, j, c):
        c += 1
        _max = c
    return _max

n = int(input())

Matrix = [["" for x in range(n)] for y in range(n)]

for _ in range(n):
    Matrix[_] = list(input())
_max = 0


for x in range(n):
    for y in range(n):
        if Matrix[x][y] == '.':
            _max = max(_max, distance(Matrix, x, y))

if _max != 0:
    print(_max - 1)
else:
    print(_max)



