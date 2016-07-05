

t = int(input())
_dict = {'(':')', '{':'}', '[':']'}
opens = ['(', '{', '[']
closes = [')', '}', ']']

for x in range(t):
    s = input()
    opens_stack = []
    close_stack = []
    wrong = False
    for e in s:
        if e in opens:
            opens_stack.append(e)
        else:
            if len(opens_stack):
                item = opens_stack[len(opens_stack) - 1]
                if _dict[item] == e:
                    opens_stack.pop()
                else:
                    wrong = True
                    break
            else:
                wrong = True
                break
    if len(opens_stack) == 0 and wrong is False:
        print("YES")
    else:
        print("NO")
