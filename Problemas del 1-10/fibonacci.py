def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        c = a + b
        a = b
        b = c
    
    return b

print("Ingresa un numero:")
num = int(input())
for j in range(num):
    print (fibonacci(j))