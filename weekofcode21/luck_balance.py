

n, k = [int(x) for x in input().split()]
ilist = []
nilist = []
r = []
for i in range(n):
    li, ti = [int(x) for x in input().split()]
    r.append(li)
    if ti:
        ilist.append(li)
    else:
        nilist.append(li)

silist = sorted(ilist)
_sum = sum(silist[len(silist) - k:]) - sum(silist[:len(silist) - k]) + sum(nilist)
print(_sum)

