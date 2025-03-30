import math
import statistics
def imprimir_numeros_en_rango(lista, rango_inferior, rango_superior):
    
    numeros_en_rango = [numero for numero in lista if rango_inferior <= numero <= rango_superior]
    
    print(f"Números en el rango [{rango_inferior}, {rango_superior}]: {numeros_en_rango}")

lista = [23, 26, 14, 36, 29, 62, 33, 49, 32, 16, 23, 56, 45, 54, 35, 31, 40, 26, 35, 49, 23, 47, 53, 47, 55, 46, 39, 25, 35, 31, 11, 40, 20, 46, 53, 32, 29, 25, 41, 51, 49, 54, 52, 24, 35, 25, 28, 51, 50, 37]
rango_inferior = 58
rango_superior = 65

print(imprimir_numeros_en_rango(lista, rango_inferior, rango_superior))

'''
x = statistics.mean(lista)
y = statistics.mode(lista)
z = statistics.median(lista)
print("x es igual a:",x)
print("y es igual a:",y)
print("z es igual a:",z)
'''
