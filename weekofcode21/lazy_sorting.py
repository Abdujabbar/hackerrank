import random


def is_not_sorted(p):
    for i in range(len(p) - 1):
        if p[i] > p[i + 1]:
            return True
    return False



d = -3
a1 = 5
