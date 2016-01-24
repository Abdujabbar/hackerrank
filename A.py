
a = input()
b = input()
aa = ''
bb = ''
ai = 0
bi = 0
while ai < len(a):
    if a[ai] == '0':
        ai += 1
    else:
        break

while bi < len(b):
    if b[bi] == '0':
        bi += 1
    else:
        break

ra = a[ai:]
rb = b[bi:]
if len(ra) > len(rb):
    print(">")
elif len(ra) < len(rb):
    print("<")
else:
    i = 0
    eq = True
    while i < len(ra):
        if ra[i] > rb[i]:
            print(">")
            eq = False
            break
        elif ra[i] < rb[i]:
            print("<")
            eq = False
            break
        i += 1
    if eq:
        print("=")
