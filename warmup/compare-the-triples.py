ar = [int(x) for x in input().split()]
br = [int(x) for x in input().split()]

alice_point = 0
bob_point = 0

for x in range(len(ar)):
    if ar[x] > br[x]:
        alice_point += 1
    elif ar[x] < br[x]:
        bob_point += 1

print(str(alice_point) + " " + str(bob_point))