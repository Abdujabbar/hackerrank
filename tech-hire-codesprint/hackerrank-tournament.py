from operator import itemgetter


n = int(input())
_dict = dict()
for _ in range(n):
    t = int(input())
    for q in range(t):
        team, s, p = [str(x) for x in input().split()]
        if team not in _dict.keys():
            _dict[team] = {"score": 0, "penalty": 0}
            _dict[team]["score"] = int(s)
            _dict[team]["penalty"] = int(p)
            _dict[team]["name"] = team
        else:
            _dict[team]["score"] += int(s)
            _dict[team]["penalty"] += int(p)

ar = []
for key, item in _dict.items():
    ar.append(item)

ar = sorted(ar, key=itemgetter('score', 'penalty'), reverse=True)
start = False
startIndex = 0
endIndex = len(ar) - 1
for x in range(1, len(ar)):
    if ar[x]["score"] == ar[x - 1]["score"] and ar[x]["penalty"] == ar[x - 1]["penalty"]:
        start = True
        startIndex = x
        continue

    if start:
        if ar[x]["score"] == ar[x-1]["score"] and ar[x]["penalty"] == ar[x-1]["penalty"]:
            endIndex = x
        else:
            start = False
            ar[startIndex:endIndex] = sorted(ar[startIndex:endIndex], key=itemgetter('name'))

current = ar[0]["score"] + ar[0]["penalty"]
c = 1
t = 1

print(t, end=" ")
print(ar[0]["name"], end=" ")
print(ar[0]["score"], end=" ")
print(ar[0]["penalty"])

for x in range(1, len(ar)):
    cc = ar[x]["score"] + ar[x]["penalty"]
    c += 1
    if cc != current:
        t = c
        current = cc
    print(t, end=" ")
    print(ar[x]["name"], end=" ")
    print(ar[x]["score"], end=" ")
    print(ar[x]["penalty"])