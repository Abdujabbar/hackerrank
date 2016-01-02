inp = input().split()
n, k, q = int(inp[0]), int(inp[1]), int(inp[2])
arr = [int(x) for x in input().split()]
l = len(arr)
d = k % l
for _ in range(q):
    idx = int(input())
    index = idx - d
    if index < 0:
        index += l
    print(arr[index])
