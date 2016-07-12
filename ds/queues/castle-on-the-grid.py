
def dfs(matrix, a, b, c, d):
    stack = []
    stack.append((a, b))
    global n
    visited = [[False for x in range(n)] for y in range(n)]
    paths = [[0 for x in range(n)] for y in range(n)]
    paths[a][b] = 1
    prev = (a, b)
    visited[a][b] = True
    c = 0
    while len(stack) != 0:
        current = stack.pop(0)
        i, j = current[0], current[1]

        if c != 0:
            paths[i][j] += paths[prev[0]][prev[1]] + 1

        c += 1
        visited[i][j] = True
        if j - 1 >= 0 and matrix[i][j - 1] == '.' and visited[i][j - 1] is False:
            stack.append((i, j))

        if j + 1 < n and matrix[i][j + 1] == '.' and visited[i][j + 1] is False:
            stack.append((i, j + 1))

        if i - 1 >= 0 and matrix[i - 1][j] == '.' and visited[i - 1][j] is False:
            stack.append((i - 1, j))

        if i + 1 < n and matrix[i + 1][j] == '.' and visited[i + 1][j] is False:
            stack.append((i + 1, j))


        prev = current

    print(paths)

n = int(input())


m = [["" for x in range(n)] for y in range(n)]

graph = {}
sets = []
for x in range(n):
    m[x] = list(input())

a, b, c, d = [int(x) for x in input().split()]

dfs(m, a, b, c, d)
