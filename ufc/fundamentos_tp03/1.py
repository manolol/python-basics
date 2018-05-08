print("Entre um numero inteiro positivo: ")
n = int(input())
s = 0
el = 1
for i in range(1, n+1):
    s += el/i
    el += 2
print("O resultado eh: {}".format(s))