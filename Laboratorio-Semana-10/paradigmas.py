#Bucle y condicional
n = int(input("Introduce hasta donde quieres imprimir: "))
for i in range(0,n):
    if n <= 0:
        print("Introduce algo bien")
    else:
        print(i)

#Funciones
def suma(n):
    sumapro = 0
    for i in range(0,n):
        sumapro = sumapro + i
    return sumapro

print(suma(n))

#Modular
import conversor
print(conversor.Kms_to_mile(n))
print(conversor.Cel_to_Faren(n))
print(conversor.Lts_to_Gal(n))

#Clases
class padre:
    def __init__(self, ojos, apellido, dinero, edad):
        self.ojos = ojos
        self.apellido = apellido
        self.dinero = dinero
        self.edad = edad

class hijo(padre):
    def __init__(self, ojos, apellido, dinero, edad, orientacion):
        super().__init__(ojos, apellido, dinero, edad)
        self.edad = edad
        self.orientacion = orientacion

Pedro = padre("cafes", "Gonzalo", "1111", "45")
Pedrito = hijo("cafes", "Gonzalo", "5 varos", "24", "gay")

#Quiero las edades del padre e hijo
print("Padre:", Pedro.edad, "Hijo:", Pedrito.edad)