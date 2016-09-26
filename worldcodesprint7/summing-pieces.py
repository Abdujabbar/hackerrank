
def calc_part(iterable, length):
    r = 0
    ii = 0
    if length > 1:
        tt = 0
        while tt < len(iterable):
            ii = tt
            while ii < len(iterable):
                aa = iterable[ii:length]
                r += sum(aa) * length
                ii += length
            tt += 1

            if ii != len(iterable):
                ii -= length
                r += sum(iterable[ii:] * (len(iterable) - ii))
    else:
        while ii < len(iterable):
            r += iterable[ii]
            ii += 1
    return r

n = int(input())

a = [int(x) for x in input().split()]

i = 1
res = 0
# r += calc_part(a, i)
while i < len(a):
    res += calc_part(a, i)
    i += 1

print(r)
