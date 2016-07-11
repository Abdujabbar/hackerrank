__author__ = 'abdujabbor'


def is_prime(n):
    if n == 2 or n == 3 or n == 5:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i =  5
    w = 2
    while i * i < n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

n, q = [int(x) for x in input().split()]
pile = [int(x) for x in input().split()]

t = 2
stack = [t]
counter = 1

while counter < q:
    t += 1
    if is_prime(t):
        stack.append(t)
        counter += 1
primes = []
for v in stack:
    non_primes = []

    while pile:
        x = pile.pop()
        if x % v == 0:
            primes.insert(x)
        else:
            non_primes.insert(x)

    pile = non_primes
    while primes:
        print(primes.pop())


while non_primes:
    print(non_primes.pop())

