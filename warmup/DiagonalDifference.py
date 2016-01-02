n = int(input())
_sum = 0
matrix_ = [[0]*n for i in range(n)]

for i in range(n):
    matrix_[i] = [int(x) for x in input().split()]


for i in range(n):
    for j in range(n):
        if i == j:
            _sum += matrix_[i][i] - matrix_[i][n - j - 1]

print(abs(_sum))D