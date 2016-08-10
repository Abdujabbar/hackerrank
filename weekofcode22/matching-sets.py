
n = int(input())

ax = [int(x) for x in input().split()]
ay = [int(y) for y in input().split()]
sumx = sum(ax)
sumy = sum(ay)
c = 0
if sumx == sumy:
    ax = sorted(ax)
    ay = sorted(ay)
    max_diff = 0
    if ay[0] > ax[0]:
        max_diff += ay[0] - ax[0]
    for x in range(1, len(ax)):
        if ay[x] > ax[x]:
            max_diff += ay[x] - ax[x]
    print(max_diff)

else:
    print(-1)