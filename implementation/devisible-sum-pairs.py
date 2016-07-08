
n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
counter = 0
for x in range(len(a)):
    for y in range(x + 1, len(a)):
        if (a[x] + a[y]) % k == 0:
            counter += 1

print(counter)