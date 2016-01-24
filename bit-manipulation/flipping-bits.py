__author__ = 'abdujabbor'


for _ in range(int(input())):
    a = int(input())
    bin_a = "{0:b}".format(a).zfill(32)
    converted_bin = ''
    for i in range(len(bin_a)):
        if bin_a[i] == '1':
            converted_bin += '0'
        else:
            converted_bin += '1'

    print(int(converted_bin, 2))
