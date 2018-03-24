#!/usr/bin/python3

# fatorial
m = int(1)
def fatorial(n) :
    global m
    if n > 1 :
        m *= n
        fatorial(n - 1)
    return m

# neper
def neper(precision) :
    # variables
    neper_n = 0
    for i in range (0, precision + 1) :
        n = fatorial(i)
        global m
        m = 1
        print("{}! = {}".format(i, n))
        neper_n += float(1 / n)
    return neper_n

precision = int(input('Type the precision: ')) 
print('Euler\'s number: {:.10f}'.format(neper(precision)))
