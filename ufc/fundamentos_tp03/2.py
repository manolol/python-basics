print("Entre um numero inteiro positivo maior ou igual a 2:")
n = int(input())
fib2 = 0
fib1 = 1
print("A sequencia de Fibonacci dos {} primeiros elementos eh:\n{}\n{}".format(n, fib2, fib1))
for i in range(1, n-1):
    fib = fib1+fib2
    print(fib)
    fib2 = fib1
    fib1 = fib
