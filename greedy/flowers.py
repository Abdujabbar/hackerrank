
_, K = [int(x) for x in input().split()]
C = sorted([int(x) for x in input().split()], reverse=True)
i = 1
p = 0
while C:
    p += sum(C[:K])*i
    print(C[:K])
    i += 1
    C = C[K:]
print(p)