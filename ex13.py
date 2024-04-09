#link http://sheilacaceres.com/courses/lpe/Lista-64Exercicios.pdf
#vou fazer um sort para resolver esse exercicio.
import random

array = []
for i in range(100):
    array.append(random.randint(0,100)) 
def buble_sort(array):
    for i in range(100 -1):
        for j in range(100-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1]= array[j+1], array[j]
    
    return array

print(buble_sort(array))
