
def bfs(graph, node):
    global mark
    global _distance
    queue=[]
    queue.append(node)
    mark[node] = 1

    while queue:
        current = queue.pop(0)

        for x in graph[current]:
            if mark[x] == 0:
                _distance[x] = _distance[current] + 6
                mark[x] = 1
                queue.append(x)


t = int(input())
_distance = []
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    _graph = {}
    _distance = [0] * n
    mark = [0] * n
    for x in range(n):
        _graph[x] = set()


    for x in range(m):
        a, b = [int(x) for x in input().split()]
        _graph[a - 1].add(b - 1)
        _graph[b - 1].add(a - 1)

    s = int(input()) - 1

    bfs(graph=_graph, node=s)

    for x in range(len(_distance)):
        if s == x:
            continue
        else:
            if _distance[x] == 0:
                print(-1, end=' ')
            else:
                print(_distance[x], end=' ')
    print()


