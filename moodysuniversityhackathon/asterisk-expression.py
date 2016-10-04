

def check_expression(expression):
    if '***' in expression:
        return False
    exp = list(expression)
    if exp[0] == '*' or exp[len(exp) - 1] == '*':
        return False

    return True


def less_than(r):
    if r >= 1000000007:
        r = r % 1000000007
    return r


def calculate_result(s):
    e = s
    _numbers = []
    _operators = []

    nstart = False
    numb = ""
    op = ""
    ostart = False
    _line = []
    for x in e:
        if x != "*":
            nstart = True
            numb += x

            if ostart:
                _operators.append(op)
                _line.append(op)
                op = ""
                ostart = False
        else:
            ostart = True
            op += x
            if nstart:
                _line.append(int(numb))
                # _numbers.append(numb)
                numb = ""
                nstart = False

    print(_line)

    # if numb:
    #     _numbers.append(numb)
    #
    # i = 0
    # r = int(_numbers.pop(0))
    # r = less_than(r)
    # while i < len(_operators) - 1 and _numbers:
    #     current_operator = _operators[i]
    #     next_operator = _operators[i + 1]
    #
    #     if current_operator == "*":
    #         if current_operator == next_operator:
    #             r = r * int(_numbers.pop(0))
    #             r = less_than(r)
    #         else:
    #             if _numbers:
    #                 rr = int(_numbers.pop(0))
    #                 j = i + 1
    #                 while next_operator == "**" and j < len(_operators) and _numbers:
    #                     nn = int(_numbers.pop(0))
    #                     if nn >= 1000000006:
    #                         nn = nn % 1000000006
    #                     rr = rr ** nn
    #                     j += 1
    #                     next_operator = _operators[j]
    #                 r = less_than(r * rr)
    #                 i = j
    #     else:
    #         while current_operator == "**" and i < len(_operators) and _numbers:
    #             nn = int(_numbers.pop(0))
    #             if nn >= 1000000006:
    #                 nn = nn % 1000000006
    #             r = less_than(r ** nn)
    #             i += 1
    #             current_operator = _operators[i]
    #
    # if _numbers and i < len(_operators):
    #     if _operators[i] == "*":
    #         r = less_than(r * int(_numbers.pop(0)))
    #     else:
    #         nn = int(_numbers.pop(0))
    #         if nn >= 1000000006:
    #             nn = nn % 1000000006
    #         r = less_than(r ** nn)
    # return r


# n = int(input())
# for _ in range(n):
#     e = input()
#     if check_expression(e):
#         print(calculate_result(e))
#     else:
#         print("Syntax Error")
