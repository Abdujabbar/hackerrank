
n = int(input())
c = 3
step = 3

i = 1
while i + step <= n:
    i += step
    step = step * 2

k = step

print(step - (n - i))
