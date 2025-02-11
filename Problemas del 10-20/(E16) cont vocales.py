frase = input('Introduce la palabra: ')
vocales = 'aeiouAEIOU'

cont=0
for i in frase:
    if i in vocales:
        cont = cont + 1

print('Tiene',cont, "vocales")