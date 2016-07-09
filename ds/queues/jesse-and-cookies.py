import heapq as pq
n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
pq.heapify(a)

c = 0

if len(a) == 0:
    print(-1)
else:
    v = pq.heappop(a)
    if len(a) > 1:
        while len(a) >= 1 and v < k:
            v2 = pq.heappop(a)
            r = v + 2 * v2
            pq.heappush(a, r)
            v = pq.heappop(a)
            c += 1

        if v >= k:
            print(c)
        else:
            print(-1)
    else:
        if v >= k:
            print(c)
        else:
            print(-1)
