__author__ = 'abdujabbor'

s = input()
pattern = 'SOS'
counter = 0
for i in range(0, len(s), 3):
    curr = s[i:i + 3]
    found = 0
    for t in range(len(pattern)):
        if pattern[t] == curr[t]:
            found += 1
    counter += (3 - found)

print(counter)
