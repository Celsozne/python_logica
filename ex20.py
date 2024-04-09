#link http://sheilacaceres.com/courses/lpe/Lista-64Exercicios.pdf

#input
array = []

a = float(input("digite um valor"))
if a <= 0:
    a= print(input("digite valores positivos"))

b = float(input("digite outro valor"))
if b <= 0:
    b= print(input("digite valores positivos"))
c = float(input("digite um terceiro valor"))
if c <= 0:
    c=print(input("digite valores positivos"))
array = [a, b ,c]
#process
def buble_sort(array):
    for i in range(3 -1):
        for j in range(3-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1]= array[j+1], array[j]
    
    return array

sorted_array= buble_sort(array)
#ele pega o maior numero do array anterior, por isso -1, achei genial, fiquei uns 20 min tentando direto no array do bubble(eu sei que ta errado no codigo)
#tentei orgranizar um pouco melhor as coisas
smallest = sorted_array[0]
largest = sorted_array[-1]
#output
print(f"o menor valor {smallest} vezes o maior {largest} sera {smallest*largest}"
      f"e a divisao entre o maior e o menor sera{largest/smallest} ")
