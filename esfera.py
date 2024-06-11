import math

raio = float(input("Informe o raio do circulo: "))

if raio <= 0:
    print("informe um valor valido")
    raio = float(input("Informe o raio do circulo: "))
else:
    volume = (3/4)*math.pi*raio*raio
    print(volume)
