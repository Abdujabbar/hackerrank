
n1, n2, n3 = [int(x) for x in input().split()]

stack1 = [int(x) for x in input().split()]
stack2 = [int(x) for x in input().split()]
stack3 = [int(x) for x in input().split()]
stacks = [stack1, stack2, stack3]
heights = [sum(stack1), sum(stack2), sum(stack3)]


while len(set(heights)) > 1:
    iheight = heights.index(max(heights))
    heights[iheight] -= stacks[iheight].pop(0)

print(heights[0])
