inventario = []

def agregar_producto():
    nombre = input("Ingrese el nombre: ")
    categoria = input("Ingrese el numero: ")
    precio = input("ingrese el correo: ")
    cantidad = input("Ingrese la cantidad: ")
    producto = (nombre.capitalize, categoria, precio, cantidad)
    inventario.append(producto)
    return "Producto agregado"

def eliminar_producto():
    nombre = input("Ingrese el nombre del prodcuto que desea eliminar:")
    for producto in inventario:
        if producto[0] == nombre.capitalize:
            inventario.remove(producto)
    return "Producto eliminado"

def buscar_info():
    nombre = input("Ingrese el nombre del prodcuto que desea eliminar:")
    for producto in inventario:
        if producto[0] == nombre.capitalize:
            print("Categoria:", producto[1], "Precio:", producto[2], "Cantidad:", producto[3])
    return "No existe o ingrese mejor el nombre"

def ordenar_inventario():
    ordenamiento = sorted(inventario, lambda x: x[0])
    for producto in ordenamiento:
        print(producto[0], producto[1], producto[2], producto[3])

accion = input("Que desea realizar: agregar un producto(1), eliminar un producto(2), buscar informacion del producto(3), ordenar inventario(4): ")
if accion == "1":
    print(agregar_producto())
elif accion == "2":
    print(eliminar_producto())
elif accion == "3":
    print(buscar_info())
elif accion == "4":
    print(ordenar_inventario())
else:
    print("Escoje bien pa")