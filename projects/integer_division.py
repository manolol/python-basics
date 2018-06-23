def division(a,b):
    remainder = a%b
    d = (a-remainder)/b
    return d

print("Enter two integer numbers:")
a = int(input())
b = int(input())
print("Result = {}".format(division(a,b)))