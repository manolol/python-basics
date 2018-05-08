#!/usr/bin/python3

while(True):
    print('Type four distinct numerical values in the same line separated by spaces:')
    a, b, c, d = input().split()
    a, b, c, d = int(a), int(b), int(c), int(d)
    if a > b:
        greater = a
        s_greater = b
    else:
        greater = b
        s_greater = a
    if greater < c:
        s_greater = greater
        greater = c
    elif s_greater < c:
        s_greater = c
    if greater < d:
        s_greater = greater
        greater = d
    elif s_greater < d:
        s_greater = d
        print(s_greater)
    print("Second greater: {}".format(s_greater))
