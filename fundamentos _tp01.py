# URI Online Judge
#1001
'''
while(True):
A = int(input())
B = int(input())
X = A + B
print("X =", X)
'''
#1002
'''
while(True):
    pi = 3.14159
    R = float(input())
    A = pi * R**2
    print("A={:.4f}".format(A))
    # or use 'print(f"A={A:.4f}")'
'''
#1003
'''
while(True):
    A = int(input())
    B = int(input())
    SOMA = A + B
    print("SOMA =", SOMA)
'''
#1004
'''
while(True):
    A = int(input())
    B = int(input())
    PROD = A * B
    print("PROD =", PROD)
'''
#1005
'''
while(True):
    A = float(input())
    B = float(input())
    MEDIA = (A*3.5 + B*7.5)/11
    print("MEDIA = {:.5f}".format(MEDIA))
'''
#1006
'''
while(True):
    A = float(input())
    B = float(input())
    C = float(input())
    MEDIA = (A*2+ B*3+C*5)/10
    print("MEDIA = {:.1f}".format(MEDIA))
'''
#1007
'''
while(True):
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    DIFERENCA = A*B-C*D
    print("DIFERENCA =", DIFERENCA)
'''
#1008
'''
while(True):
    number = int(input())
    worked_hours = int(input())
    amount_per_hour = float(input())
    salary = amount_per_hour*worked_hours
    print("NUMBER =", number)
    print("SALARY = U$ {:.2f}".format(salary))
'''
#1009
'''
while(True):
    first_name = str(input())
    salary = float(input())
    sold = float(input())
    salary+=sold*0.15
    print("TOTAL = R$ {:.2f}".format(salary))
'''
#1010
'''
while(True):
    code1, units1, price1 = input().split()
    code2, units2, price2 = input().split()
    total = int(units1)*float(price1) + int(units2)*float(price2)
    print("VALOR A PAGAR: R$ {:.2f}".format(total))
'''
#1011
'''
while(True):
    pi =  3.14159
    radius = float(input())
    volume = (4/3) * pi * radius**3
    print("VOLUME = {:.3f}".format(volume))
'''
#1012
'''
while(True):
    A, B, C = input().split()
    A, B, C = float(A), float(B), float(C)
    triangle = (A*C)/2
    circle = 3.14159 * C**2
    trapezium = ((A + B)*C)/2
    square = B**2
    rectangle = A*B
    print("TRIANGULO: {:.3f}".format(triangle))
    print("CIRCULO: {:.3f}".format(circle))
    print("TRAPEZIO: {:.3f}".format(trapezium))
    print("QUADRADO: {:.3f}".format(square))
    print("RETANGULO: {:.3f}".format(rectangle))
'''
#1013
'''
while(True):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    absAB = 0
    absABC = 0
    if a-b < 0:
        absAB = b-a
    else:
        absAB = a-b
    greatestAB = (a+b+absAB)/2
    if(greatestAB - c < 0):
        absABC = c - greatestAB
    else:
        absABC = greatestAB - c
    greatest = int((greatestAB + c + absABC)/2)
    print(greatest, "eh o maior")
'''
#1014
'''
while(True):
    X = int(input())
    Y = float(input())
    CONSUMPTION = X/Y
    print("{:.3f} km/l".format(CONSUMPTION))
'''
#1015
'''
while(True):
    x1, y1 = input().split()
    x2, y2 = input().split()
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print("{:.4f}".format(distance))
'''
#1016
'''
while(True):
    km = int(input())
    print(2*km, "minutos")
'''