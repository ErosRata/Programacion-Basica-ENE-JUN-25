def raices_cuadraticas(a,b,c):
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + D**(1/2))/(2*a)
        x2 = (-b - D**(1/2))/(2*a)
        return x1,x2
    elif D == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + D**(1/2))/(2*a)
        x2 = (-b - D**(1/2))/(2*a)
        return x1,x2

a = float(input("Introduce el coeficiente cuadratico:" ))
b = float(input("Introduce el coeficiente lineal:" ))
c = float(input("Introduce el coeficiente independiente:" ))
print(raices_cuadraticas(a,b,c))