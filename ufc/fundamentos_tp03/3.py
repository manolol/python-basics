print("Entre um numero inteiro positivo:")
n = int(input())
fib2 = 0
fib1 = 1
i = 0
fib = 1 # a sequecia comeca com 1 nessa questao, como falado em sala
if n < 2:
    print("Nao existem numeros na sequencia de Fibonacci menores do que {}".format(n))
else:
    print("A sequencia de Fibonacci com os elementos da sequencia menores do que {} eh:".format(n))
while fib < n:
    print(fib)
    fib = fib1+fib2
    fib2 = fib1
    fib1 = fib