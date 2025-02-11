a = int(input('Ingresa un 1er numero: '))
b = int(input('Ingresa un 2do numero: '))
c = int(input('Ingresa un 3er numero: '))

if  a > b:
    if a > c:
        print(a)
    else: print(c)
elif b > c:
    print(b)
else: print(c)