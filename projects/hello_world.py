#!/usr/bin/python3
# the line above specifies the interpreter

## comments
# a comment
"""
    a
    multiple
    line
    comment
"""

## primitive types
integer = int() # integer = 1 # you can treat strings as numbers
real = float() # real = 1.
string = str() # string = '1'
boolean = bool(True)

## variables
number = 1.e5 # scientific notation, it prints 100000
# print(number)

## operations
division = 10/3 # it returns the result as real number
# print(division)

## strings
print('---strings---')
string_2 = """
    ---begin---\n
    This is a long text with multiple lines\n
    ---end---
"""
print(string_2)
print(len(string_2)) # length of string_2
print(string_2.upper()) # all letters upper case (capitalize)
print(string_2.lower()) # all letters lower case
# to combine a string with variables (formating)
name = 'Robert'
age = 22
print('Doctor %s. He\'s %d' % (name, age))
day = 2
print('Today\'s %02d' % (day)) # 0 -> pad with zeros, 2 -> two wide
# or
print('(Newer way) Today\'s {:02d}'.format(day));

## functions
def sum(x, y) :
    print("Sum:")
    return a + b

def times(x, y) :
    print("Times:")
    return a * b

# using global variables inside a function
global_var = 'some_value'
def print_var() :
    global global_var
    return global_var

def print_message() : # function names should be lowercase, with words separated by underscores as necessary to improve readability
    message = "end"
    print(message)

"""
a = int(input("Enter the firt number: "))
b = int(input("Enter the second number: "))
print("The result is: ")
print(sum(a, b))
print(times(a, b))
print_message()
"""

## lists
"""
list = []
print("Type values and press enter to add values to the list, type '-1' to print the complete list:")
while(1):
    n = int(input())
    if(n == -1):
        break
    list.append(n)
print(list)
"""

## date and time library
from datetime import datetime
now = datetime.now()
print('Complete date: {}\nDay: {}\nMonth: {}\nYear: {}'.format(now, now.day, now.month, now.year))

## conditionals
# if, elif, else

## boolean operators
# and, or, not

