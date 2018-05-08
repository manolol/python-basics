print("Entre um numero inteiro positivo:")
n = int(input())
print("Entre {} numeros quaisquer:".format(n))
maior = float(input())
menor = float(input())
soma = maior + menor
if maior < menor:
    aux = maior
    maior = menor
    menor = aux
for i in range(1, n-1):
    m = float(input())
    soma += m
    if maior < m:
        maior = m
    if menor > m:
        menor = m
media = soma/n
if maior == menor:
    print("Todos os numeros entrados sao iguais a {}".format(maior))
else:
    print("O maior valor eh {}".format(maior))
    print("O menor valor eh {}".format(menor))
print("A media dos valores eh {}".format(media))