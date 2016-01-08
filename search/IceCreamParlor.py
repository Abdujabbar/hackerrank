__author__ = 'abdujabbor'

for _ in range(int(input())):
    m = int(input())
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == m:
                print(str(i + 1) + " " + str(j + 1))
