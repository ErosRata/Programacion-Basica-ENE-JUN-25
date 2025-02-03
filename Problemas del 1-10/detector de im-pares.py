num = int(input('Introduce un numero cualquiera: '))

detector = num % 2

if detector == 0:
    print('El numero es par')
else:
    print("El numero es impar")