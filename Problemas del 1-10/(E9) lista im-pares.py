limite = int(input("Introduce un numero limite a calcular: "))

print('PARES')
for i in range(0,limite,2):
    print(i)

print("----------------------------------------------------------")

print('IMPARES')
for i in range (1, limite,2):
    print(i)

#En este pido hasta que numero hago la lista, y el primer print inicio desde 0 y que se brinque 2 en 2 y va ensenar todos los pares, hay un print de la nada pero sirve para separar 
# o que sea mas "VISIBLE", esa separacion o el termino de la 1ra lista, abajo inicio desde 1 e igual los brincos de 2 en 2 para ensenar los impares.