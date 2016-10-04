import operator
n, k = [int(x) for x in input().split()]

pi = [float(x) for x in input().split()]

xi = [float(x) for x in input().split()]

yi = [float(x) for x in input().split()]

expactedProfit = []

for i in range(len(pi)):
    r = round((pi[i] * xi[i]), 2) - round((1 - pi[i]) * yi[i], 2)
    if r < 0:
        r = 0
    expactedProfit.append(r)

sortedExpactedProfit = sorted(expactedProfit, reverse=True)

r = 0
for i in range(k):
    r += sortedExpactedProfit[i]

print("%.2f" % r)
