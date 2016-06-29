
x1, v1, x2, v2 = [int(x) for x in input().split()]


if v2 < v1:
	if (x2 - x1) % (v2 - v1) == 0:
		print("YES")	
	else:
		print("NO")
else:
	print("NO")