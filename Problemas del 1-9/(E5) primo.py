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

#Es simple, un numero primo es divisible por el 1 y si mismo, osea 2 numeros solamente, entonces hay que usar un modulo y contador de modulo cuando sea 0 y si el contador 
# solo cuenta dos veces el residuo cero va decir que es primo, si no, pues no lo es y ya.
