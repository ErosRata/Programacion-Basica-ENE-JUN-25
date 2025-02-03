num1 = int(input('Introduzca el 1er numero: '))
num2 = int(input('Introduzca el 2do numero: '))

operacion = int(input('Introduzca la operacion a realizar (suma=1, resta=2, nultiplicacion=3, division=4): '))
if operacion == 1:
        suma = num1 + num2
        print(suma)
elif operacion == 2:
          resta = num1 - num2
          print(resta)
elif operacion == 3:
          multiplicacion = num1 * num2
          print (multiplicacion)
elif operacion == 4:
          division = num1 / num2
          print(division)
else:
        print('No valido apa')