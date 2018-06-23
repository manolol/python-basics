def fatorial(n):
    if n == 1:
        return n
    else:
        return n*fatorial(n-1)

print("Enter a number:")
n = int(input())
r = fatorial(n)
print("The result is: {}".format(r))