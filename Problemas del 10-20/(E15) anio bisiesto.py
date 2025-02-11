anio = int(input('Introduce el anio a determinar: '))

bisiesto = anio % 4
if bisiesto == 0:
    print('El anio es bisiesto')
else: print('No es bisiesto')