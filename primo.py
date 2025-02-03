num = int(input("Ingresa un numero: "))
i = 1
cont = 0
while i <= num:
    if num % i == 0:
        cont = cont + 1
    i = i + 1
if cont == 2:
    print("El numero es primo apa")
else:
    print("No es primo apa")