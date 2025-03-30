def estadistica(*args):
    promedio = lambda x: sum(x)/len(x)
    mediana = lambda x: x[len(x)//2]
    suma = 0
    for i in range (len(args)):
        suma += (args[i] - promedio(args))**2
    destan=(suma/len(args))**(1/2)
    return promedio(args), mediana(args), destan

n = int(input("Cuanto numeros deseas ingresar: "))
lista = []
for i in range(n):
    x = float(input("Introduce un numero: "))
    lista.append(x)

resultado = estadistica(*lista)
print("El promedio es:",resultado[0], "La mediana es:",resultado[1] ,"La desviacion estandar:",resultado[2])