#algoritnmo que determina em qual quadrante o ponto definiido pelo usuario esta

x= int(input("deifina o ponto x: "))
y= int(input("defina o ponto y: "))

if x < 0 and y <0:
    print("Terceiro quadrante")
elif x>0 and y>0:
    print("Primeiro quadrante")
elif x < 0 and y>0:
    print("Segundo quadrante")
else:
    print("Quarto quadrante")

#link http://sheilacaceres.com/courses/lpe/Lista-64Exercicios.pdf