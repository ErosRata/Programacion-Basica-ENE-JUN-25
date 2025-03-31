with open("agenda", "r") as f:
    agenda_contactos = eval(f.read())

def nuevo_contacto():
    nombre = input("Ingrese el nombre: ")
    numero = input("Ingrese el numero: ")
    correo = input("ingrese el correo: ")
    contacto = (nombre.capitalize(), numero, correo)
    agenda_contactos.append(contacto)
    return "Contacto agregado"

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto que esta buscando:")
    for contacto in agenda_contactos:
        if contacto[0] == nombre.capitalize():
            return contacto
    return "Contacto no encontrado"

def ordenar_contactos():
    ordenamiento = sorted(agenda_contactos, key=lambda x: x[0])
    for contacto in ordenamiento:
        print(contacto[0],contacto[1],contacto[2])

accion = input("Que desea realizar: agregar nuevo contacto(1), buscar un contacto(2), ordenar la agenda en orden alfabetico(3): ")
if accion == "1":
    print(nuevo_contacto())
elif accion == "2":
    print(buscar_contacto())
elif accion == "3":
    print(ordenar_contactos())
else:
    print("Escoje bien pa")

with open("agenda", "w") as f:
    f.write(str(agenda_contactos))