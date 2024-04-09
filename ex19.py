#link http://sheilacaceres.com/courses/lpe/Lista-64Exercicios.pdf

L1 = float(input("tamanho do lado 1: "))
L2 = float(input("tamanho do lado 2: "))
L3 = float(input("tamanho do lado 3: "))

if L1 == L2 and L2 == L3 and L1==L3:
    print(f"o triangulo e equilatero de lado {L1}")
elif L1 == L2 and L2!=L3 and L1!=L3:
    print(f"o triangulo e isosceles dois lados de {L1} e um de lado {L3}")

elif L1 == L3 and L2 != L3 and L1 !=L2:
    print(f"o triangulo e isosceles dois lados de {L1} e outro de {L2}")

elif L1!=L2 and L1!=L3 and L3 == L2:
    print(f"o triangulo e isosceles dois lados de {L3} e outro de {L1}")

else: print("O triangulo e escaleno")