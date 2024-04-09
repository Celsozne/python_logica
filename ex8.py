import math

#estamos lidando com um cilindro portanto devemos nos preocupar
#com a area da base inicialmente
r = float(input("qual o raio da base da lata"))

#a area da base e descrita por pi*r^2

Ab = math.pi * (r**2)

#a altura e o ultimo fator para determinarmos o valume da lata

h = float(input("Qual e a altura da lata"))

# o volume da lata e definido por pi*r^2*h

V = Ab * h
print(f"O volume da lata sera {V}")

#link http://sheilacaceres.com/courses/lpe/Lista-64Exercicios.pdf