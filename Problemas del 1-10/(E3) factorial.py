print("Ingrese un numero:")
num = int(input())
fact = 1
for i in range(1, num+1):
    fact*=i
print("El factorial de",num, "es:", fact)

#Este investigue en internet y es en la linea 5 donde vi eso que puede multiplicar a nada y lo va hacer el factorial
