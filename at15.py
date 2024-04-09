import math 
area = float(input("qual o tamanho da area"))

latas = math.ceil(area/54)
preco = latas * 80

print(f"voce precisara de {latas:.0f} latas, custando R${preco:.2f}")


