__author__ = 'abdujabbor'


t = int(input())
for _ in range(t):
    a, b = [int(x) for x in input().split()]
    if a & 1:
        if b & 1:
            print("black")
        else:
            print("red")
    else:
        if b & 1:
            print("red")
        else:
            print("black")
