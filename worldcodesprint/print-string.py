__author__ = 'abdujabbor'

t = int(input())
for i in range(t):
    n, a, b = [int(x) for x in input().split()]
    s = input()
    r = s[0]
    j = 1
    aa = min(a, b)
    bb = max(a, b)
    _sum = aa
    while j < len(s):
        if j + len(r) < len(s):
            pattern = s[j:j + len(r)]
        else:
            pattern = s[j:]
        if len(pattern) == 1:
            r += s[j]
            _sum += aa
            j += 1
        else:
            lp = len(pattern)
            while lp != 1:
                if pattern[:lp] in r and pattern[:lp] == s[j:j+lp]:
                    r += pattern[:lp]
                    _sum += bb
                    j += lp
                    break
                else:
                    lp -= 1
            if lp == 1:
                r += s[j]
                _sum += aa
                j += 1

    print(_sum)
