

# n = int(input())
# y = [int(x) for x in input().split(" ")]
# st = [(0,-1)]
#
# days, maxDays = -1, -1
# for i in range(n):
#     days = 1
#     while st and y[st[-1][0]] >= y[i]:
#         days = max(days, st[-1][1]+1)
#         st.pop()
#     if not st: days = -1
#     if days > maxDays: maxDays = days
#     st.append((i, days))
# if maxDays == -1: maxDays = 0
# print(maxDays)


n = int(input())
ar = [int(x) for x in input().split()]
days = [0] * n
maxdays = 0
stack = []
min = ar[0]
stack.append(0)

for x in range(1, n):
    if ar[x] > ar[x - 1]:
        days[x] = 1

    if min > ar[x]:
        min = ar[x]

    while len(stack) != 0 and ar[stack[len(stack) - 1]] >= ar[x]:
        if ar[x] > min:
            if days[x] < days[stack[len(stack) - 1]] + 1:
                days[x] = days[stack[len(stack) - 1]] + 1
        stack.pop()

    maxdays = max(maxdays, days[x])
    stack.append(x)

print(maxdays)
