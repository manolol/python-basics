#!/usr/bin/python3

while(True):
    print('Type four distinct numerical values in the same line separated by spaces:')
    a, b, c, d = input().split()
    a, b, c, d = int(a), int(b), int(c), int(d)
    if (a < b and a > c and a > d) or (a < c and a > b and a > d) or (a < d and a > b and a > c):
        print("Second greater: {}".format(a))
    elif (b < a and b > c and b > d) or (b < c and b > a and b > d) or (b < d and b > a and b > d):
        print("Second greater: {}".format(b))
    elif (c < a and c > b and c > d) or (c < b and c > a and c > d) or (c < d and c > a and c > b):
        print("Second greater: {}".format(c))
    else:
        print("Second greater: {}".format(d))