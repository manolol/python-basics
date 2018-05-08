print("Entre um numero inteiro nao negativo:")
n = int(input())
quadrado_perfeito = False
i = 1
while(i*i <= n and quadrado_perfeito == False):
    if(i*i == n):
        quadrado_perfeito = True
    i += 1
if quadrado_perfeito:
    print("{} eh quadrado perfeito".format(n))
else:
    print("{} nao eh quadrado perfeito".format(n))
