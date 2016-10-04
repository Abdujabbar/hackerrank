
n = int(input())

x = 0
c = 0
while x <= n:

    if x + n == n ^ x:
        c += 1
        print("{0:b}".format(x))

    x += 1
print(c)
