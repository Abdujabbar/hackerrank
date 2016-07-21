
def find_devision(n):
    devision = []
    for i in range(2, n):
        if i * i >= n:
            break
        if n % i == 0:
            devision.append(i)
    return devision


q = int(input())

for _ in range(q):
    n = int(input())
    devations = find_devision(n)
    c = 0
    if devations:
        v = devations.pop()
        n = v
        c += v
        while n != 0 and devations:
            devations = find_devision(n)
            if len(devations) == 0:
                break
            v = devations.pop()
            n = v
            c += 1

    while n != 0:
        n -= 1
        c += 1

    print(c)