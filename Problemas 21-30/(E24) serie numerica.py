print("Introduce la cantidad de numeros a sumar")
n = int(input())
c = 0
num = 0
for i in range (1, n+1):
    num = float(input("Introduce un numero que tu quieras: "))
    c = c + num
print(c)
