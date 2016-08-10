
n = int(input())

ax = [int(x) for x in input().split()]
ay = [int(y) for y in input().split()]

c = 0
i = 0

while i < len(ax) - 1:
    diff = ax[i] - ay[i]
    j = i + 1
    while j < len(ax):
        rdiff = ay[j] - ax[j]
        if rdiff == diff and diff != 0:
            ax[i] -= diff
            ax[j] += diff
            c += diff
            break
        j += 1
    i += 1


found = True
for i in range(len(ax)):
    if ax[i] != ay[i]:
        found = False

if found:
    print(c)
else:
    print(-1)

