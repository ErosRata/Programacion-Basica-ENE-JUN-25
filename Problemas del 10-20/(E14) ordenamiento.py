def ordenamiento(lista):
    n = len(lista)
    for i in range(n - 1): 
        for j in range(n - 1 - i): 
            if lista[j] > lista[j + 1]:  
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  
    return lista

numeros = [45, 23, 75, 67, 12]
print("Lista ordenada:", ordenamiento(numeros))