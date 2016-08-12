from itertools import combinations

L=[1,2,3,4]

[",".join(map(str,comb)) for comb in combinations(L, 3)]
['1,2,3', '1,2,4', '1,3,4', '2,3,4']


#
# n, m = [int(x) for x in input().split()]
#
# u = [0] * m
#
# for x in range(m):
#     line = input().split()
#
#     if int(line[0]) == 1:
#         lst = list(line[2])
#         for y in range(len(lst)):
#             v = int(lst[y])
#             if v == 1:
#                 u[y] = int(line[1])
#     elif int(line[0]) == 2:
#         lst = list(line[2])
#         vv = int(lst[1])
#         for y in range(len(lst)):
#             v = int(lst[y])
#             if v:
#                 # noinspection PyAugmentAssignment
#                 u[y] = vv ^ u[y]
#         pass
#     else:
#         pass
#