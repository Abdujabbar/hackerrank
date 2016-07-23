__author__ = 'abdujabbor'

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


def is_polindrome(s):
    return s == s[::-1]
# print long_substr(['bac', 'bac'])

t = int(raw_input())
for _ in range(t):
    s1 = raw_input()
    s2 = raw_input()
    if s1 == s2:
        s1 = sorted(list(s1))
        s2 = sorted(list(s2), reverse=True)
        r = ""
        res = []
        p = 0
        q = 0
        f = False
        while p < len(s1) and q < len(s2):
            if s1[p] <= s2[q]:
                r += s1[p]
                p += 1
            else:
                r += s2[q]
                q += 1
            if len(r) > 1 and is_polindrome(r):
                res.append(r)
                r = ""
        print(res)
        print(r)
    else:

        lcs = long_substr([s1, s2[::-1]])
        if len(lcs) == 0:
            print(-1)
        else:
            print(lcs)
