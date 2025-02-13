pila = [1,2,3]

#Agregar elementos
pila.append(438)
#Quitar ultimo elemento
pila.pop()

print(pila)

from collections import deque

separar = deque("abcdef")
separar.appendleft("xd")
separar.append("ghijk")
print(separar)