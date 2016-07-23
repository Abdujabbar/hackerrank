__author__ = 'abdujabbor'


s = input()
c = 1
for x in s:
    if ord(x) >= ord('A') and ord(x) <= ord('Z'):
        c += 1

print(c)
