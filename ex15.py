#link http://sheilacaceres.com/courses/lpe/Lista-64Exercicios.pdf

n1 = float(input(" Nota do primeiro bimestre: "))
n2 = float(input("Nota do segundo bimestre: "))
n3 = float(input("Nota do terceiro bimestre: "))
n4 = float(input("Nota do quarto bimestre: "))

media = (n1 + n2 +n3 +n4)/4

if media < 6:
    print(f"sua media foi {media} entao estas reprovado")
else:
    print(f"Sua media foi {media} entao estas aprovado")