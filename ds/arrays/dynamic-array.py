__author__ = 'abdujabbor'


n, q = [int(x) for x in input().split()]
seqList = [[] for x in range(n)]
lastAns = 0

for i in range(q):
    s, x, y = [int(x) for x in input().split()]
    if s == 1:
        seq = seqList[(x ^ lastAns) % n]
        seq.append(y)
    else:
        seq = seqList[(x ^ lastAns) % n]
        lastAns = seq[y % len(seq)]
        print(lastAns)
