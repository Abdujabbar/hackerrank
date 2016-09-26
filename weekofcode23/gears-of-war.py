__author__ = 'abdujabbor'


q = int(input())

for _ in range(q):
    t = int(input())
    if t & 1:
        print("No")
    else:
        print("Yes")
