n = int(input())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in range(n):
    t = int(input())
    s = input()
    ss = dict()
    alpha_found = False
    empty_found = False
    for c in s:
        if c == '_':
            empty_found = True
        if c in alpha:
            alpha_found = True
        if c in ss.keys():
            ss[c] += 1
        else:
            ss[c] = 1

    if alpha_found:
        f = True
        if empty_found:
            for cc in alpha:
                if cc in ss.keys():
                    if ss[cc] == 1:
                        f = False
            if f:
                print("YES")
            else:
                print("NO")
        else:
            sarr = list(s)
            ff = True
            for x in range(1, len(sarr) - 1):
                if sarr[x - 1] != s[x] and s[x + 1] != s[x]:
                    ff = False
                    break
            if ff:
                print("YES")
            else:
                print("NO")
    else:
        print("YES")
