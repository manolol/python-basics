print("Entre um numero inteiro:")
n = int(input())
existe_m_primo = False
for i in range(1, n):
    count = 0
    for j in range(1, i+1):
        if(i%j == 0):
            count += 1
    if(count == 2):
        m_primo = i
        existe_m_primo = True
if existe_m_primo:
    print("O maior numero primo menor que {} eh {}.".format(n, m_primo))
else:
    print("Nao existe numero primo menor que {}".format(n))