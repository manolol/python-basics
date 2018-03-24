#!/usr/bin/python3

# b to decimal
validate = bool(1)
while(validate):
    number = input("Type a number: ")
    base = int(input("Type its base: "))
    number_c = int(number, base)
    print("The number in decimal base is: " + str(number_c))