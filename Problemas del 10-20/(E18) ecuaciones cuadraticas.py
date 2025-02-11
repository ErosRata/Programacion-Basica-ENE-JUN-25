a = int(input('Ingresa el termino cuadratico: '))
b = int(input('Ingresa el termino lineal: '))
c = int(input('Ingresa el termino independiente: '))

x1 = (-b+(b**2-4*a*c)**0.5)/2*a
x2 = (-b-(b**2-4*a*c)**0.5)/2*a

print (x1,x2)