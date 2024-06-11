import math

# Solicita os valores de a, b, c e x do usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Calcula o discriminante (delta)
delta = b**2 - 4*a*c

# Verifica se o discriminante é negativo, zero ou positivo
if delta < 0:
    print("A equação não possui raízes reais.")
else:
    # Calcula as raízes usando a fórmula quadrática
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("As raízes da equação são:", x1, "e", x2)
