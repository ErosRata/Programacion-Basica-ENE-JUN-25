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

#Este problema ya lo habia hecho en metodologia y tenia la idea clara pero no la sintaxis y aprendi usar el def, tambien investigue en internet mas que en el interior
