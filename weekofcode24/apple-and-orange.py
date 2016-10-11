#!/bin/python3


s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

apple_counter = 0
orange_counter = 0


for x in apple:
    r = a + x
    if s <= r <= t:
        apple_counter += 1

for y in orange:
    r = b + y
    if s <= r <= t:
        orange_counter += 1

print(apple_counter)
print(orange_counter)
