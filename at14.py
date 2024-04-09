peso = float(input("a pesca em kg: "))

excesso = peso - 50

if excesso > 0:
    multa = excesso * 4
    print(f"voce sera multado em R${multa}")
else: print("voce nao sera multado")