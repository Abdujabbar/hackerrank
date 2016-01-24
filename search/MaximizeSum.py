__author__ = 'abdujabbor'


def maxSubArraySum(a,size):

    max_so_far = 0
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far

for _ in range(int(input())):
    a = [int(x) for x in input().split()]
    print(maxSubArraySum(a, len(a)))
