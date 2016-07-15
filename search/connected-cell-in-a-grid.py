def bfs(matrix, m, n, i, j):
    global visited
    queue = []
    queue.append((i, j))
    counter = 0
    while queue:
        a, b = queue.pop()
        if visited[a][b]:
            continue
        visited[a][b] = 1

        if a + 1 < m and visited[a + 1][b] == 0 and matrix[a + 1][b] == 1:
            queue.append((a + 1, b))

        if a - 1 >= 0 and visited[a - 1][b] == 0 and matrix[a - 1][b] == 1:
            queue.append((a - 1, b))

        if b + 1 < n and visited[a][b + 1] == 0 and matrix[a][b + 1] == 1:
            queue.append((a, b + 1))

        if b - 1 >= 0 and visited[a][b - 1] == 0 and matrix[a][b - 1] == 1:
            queue.append((a, b - 1))

        if a + 1 < m and b + 1 < n and visited[a + 1][b + 1] == 0 and matrix[a + 1][b + 1] == 1:
            queue.append((a + 1, b + 1))

        if a + 1 < m and b - 1 >= 0 and visited[a + 1][b - 1] == 0 and matrix[a + 1][b - 1] == 1:
            queue.append((a + 1, b - 1))

        if a - 1 >= 0 and b - 1 >= 0 and visited[a - 1][b - 1] == 0 and matrix[a - 1][b - 1] == 1:
            queue.append((a - 1, b - 1))

        if a - 1 >= 0 and b + 1 < n and visited[a - 1][b + 1] == 0 and matrix[a - 1][b + 1] == 1:
            queue.append((a - 1, b + 1))

        counter += 1
    return counter

m = int(input())
n = int(input())
visited = [[0 for x in range(n)] for y in range(m)]
a = [[0 for x in range(n)] for y in range(m)]

for x in range(m):
    a[x] = [int(z) for z in input().split()]

_max = 0
for x in range(m):
    for y in range(n):
        if a[x][y] != 0 and visited[x][y] == 0:
            _max = max(_max, bfs(a, m, n, x, y))


print(_max)








