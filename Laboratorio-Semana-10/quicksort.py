import random

def lista_random(tamano, minimo, maximo):
    return [random.randint(minimo, maximo) for _ in range(tamano)]

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quicksort(izquierda) + medio + quicksort(derecha)

tamano_lista = int(input("Ingrese el tamaño de la lista: "))
lista = lista_random(tamano_lista, 1, 100)

lista_ordenada = quicksort(lista)
print(lista)
print(lista_ordenada)


