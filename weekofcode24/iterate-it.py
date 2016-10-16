import time

start = time.time()

n = int(input())

arr = [int(x) for x in input().split()]

rep = 0
timedout=False
while True:
    if len(arr) == 0:
        break
    b = []
    x = len(arr) - 1
    y = 0
    i = 0
    f = False
    while x >= 0:
        for i in range(x):
            if arr[x] != arr[i]:
                b.append(abs(arr[x] - arr[i]))
        x -= 1

    arr = b
    rep += 1
    end = time.time()
    if end - start >= 10:
        timedout = True
if timedout:
    print(-1)
else:
    print(rep)
