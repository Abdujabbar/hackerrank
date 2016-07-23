__author__ = 'abdujabbor'

def calc_facto(n):
    t = 1
    r = 1
    while t <= n:
        r *= t
        t += 1

    return r


a = calc_facto(3)
b = calc_facto(4)

