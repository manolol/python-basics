#!/usr/bin/python3

while(True):
    print('Type four distinct numerical values in the same line separated by spaces:')
    a, b, c, d = input().split()
    a, b, c, d = int(a), int(b), int(c), int(d)
    # first scan
    if(a > b):
        aux = a
        a = b
        b = aux
    if(b > c):
        aux = b
        b = c
        c = aux
    if(c > d):
        aux = c
        c = d
        d = aux
    # second scan
    if(a > b):
        aux = a
        a = b
        b = aux
    if(b > c):
        aux = b
        b = c
        c = aux
    if(c > d):
        aux = c
        c = d
        d = aux
    # third scan
    if(a > b):
        aux = a
        a = b
        b = aux
    if(b > c):
        aux = b
        b = c
        c = aux
    if(c > d):
        aux = c
        c = d
        d = aux
    print("Second greater: {}".format(c))