t = int(input())
for i in range(t):
    s = input()
    r = s[::-1]
    not_funny = False
    for j in range(1, len(s)):
        d1 = abs(ord(s[j]) - ord(s[j - 1]))
        d2 = abs(ord(r[j]) - ord(r[j - 1]))
        if d1 != d2:
            not_funny = True
            break
    
    if not_funny:
        print("Not Funny")
    else:
        print("Funny")