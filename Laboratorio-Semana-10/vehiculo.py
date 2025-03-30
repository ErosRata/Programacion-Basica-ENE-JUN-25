class vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def mostrar(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año", self.anio)
        print("Precio", self.precio)

class automovil(vehiculo):
    def __init__(self, marca, modelo, anio, precio, puertas):
        super().__init__(marca, modelo, anio, precio)
        self.puertas = puertas

    def mostrar(self):
        super().mostrar()
        print("Numero de puertas", self.puertas)

class motocicleta(vehiculo):
    def __init__(self, marca, modelo, anio, precio, cilindrada):
        super().__init__(marca, modelo, anio, precio)
        self.cilindrada = cilindrada

    def mostrar(self):
        super().mostrar()
        print("Cilindrada", self.cilindrada)

Tsuru = automovil("Nissan", "Tsuru", "1997", "25000", "4")
Tsuru.mostrar()
print("-----------------------------------------------------------------------------------------------------------------------------------------")
Bmw = motocicleta("BMW", "nose el modelo", "2019", "100000", "625")
Bmw.mostrar()