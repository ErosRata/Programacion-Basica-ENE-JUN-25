def buscar(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return print("no")
    
numeros = [4, 2, 9, 1, 5, 6]
print(buscar(numeros, 2))