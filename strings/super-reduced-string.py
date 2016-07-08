
input = input()


stack = []
stack.append(input[0])

for x in range(1, len(input)):
    if len(stack) and stack[len(stack) - 1] == input[x]:
        stack.pop()
    else:
        stack.append(input[x])


if stack:
    print("".join(stack))
else:
    print("Empty String")
