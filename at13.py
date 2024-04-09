altura = float(input("sua altura e: "))
genero = input("qual o seu genero")
genero1 = "homem"
genero2 = "mulher"

if genero == genero1:
    pesoid1 = (altura * 72.2) - 58
    print(f"seu peso ideal e: {pesoid1}")

else:pesoid2 = (62.1 *altura) -44.7
print(f"seu peso ideal e: {pesoid2}")

