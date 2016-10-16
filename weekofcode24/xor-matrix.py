n, m = [int(x) for x in input().split()]

ar = [int(x) for x in input().split()]
row0 = ar
row_zeros = [0] * n
zeros_found = False
arrs = [ar]
if len(ar) > 1:
    i = 1
    r = -1
    while i < m:
        br = []
        for x in range(len(ar) - 1):
            br.append(ar[x] ^ ar[x + 1])
        br.append(ar[0] ^ ar[len(ar) - 1])
        i += 1

        for index in range(len(arrs) - 1, 0, - 1):
            if arrs[index] == br:
                r = len(arrs) - index
        if r != -1:
            break
        ar = br
        arrs.append(ar)

    if r != -1:
        ar = row0
        m = m % r
        i = 1
        while i < m:
            br = []
            for x in range(len(ar) - 1):
                br.append(ar[x] ^ ar[x + 1])
            br.append(ar[0] ^ ar[len(ar) - 1])
            i += 1
            if br == row_zeros:
                zeros_found = True
                break
            ar = br

if zeros_found:
    ar = row_zeros

for x in ar:
    print(x, end=' ')
