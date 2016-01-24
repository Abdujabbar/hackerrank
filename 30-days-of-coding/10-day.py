__author__ = 'abdujabbor'




for _ in range(int(input())):
    n = int(input())
    r = ''
    while n >= 1:
        if n % 2 == 0:
            r += '0'
        else:
            r += '1'
        n = int(n/2)
    print("".join(reversed(r)))