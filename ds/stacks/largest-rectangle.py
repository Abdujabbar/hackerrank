

n = int(input())
h = [int(x) for x in input().split()]

stack = []
max_area = 0
i = 0
while i < n:
    if len(stack) == 0 or h[i] >= h[stack[len(stack) - 1]]:
        stack.append(i)
        i += 1
    else:
        t = stack.pop()
        if len(stack) == 0:
            area = h[t] * i
        else:
            area = h[t] * (i - stack[len(stack) - 1] - 1)
        max_area = max(max_area, area)




while len(stack) != 0:
    t = stack.pop()
    if len(stack) == 0:
        area = h[t] * i
    else:
        area = h[t] * (i - stack[len(stack) - 1] - 1)
    max_area = max(max_area, area)

print(max_area)