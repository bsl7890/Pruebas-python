import os
def opcio1(cantidad):
    precio = 700
    precioFinal = precio * cantidad
    print(f"Precio a pagar: {precioFinal}")
    input("presione cualquier tecla para continuar.......")
def opcio2(cantidad):
    precio = 500
    precioFinal = precio * cantidad
    print(f"Precio a pagar: {precioFinal}")
    input("presione cualquier tecla para continuar.......")
def opcio3(cantidad):
    precio = 2500
    precioFinal = precio * cantidad
    print(f"Precio a pagar: {precioFinal}")
    input("presione cualquier tecla para continuar.......")
def opcio4(cantidad):
    precio = 1000
    precioFinal = precio * cantidad
    print(f"Precio a pagar: {precioFinal}")
    input("presione cualquier tecla para continuar.......")
def opcio5(cantidad):
    precio = 800
    precioFinal = precio * cantidad
    print(f"Precio a pagar: {precioFinal}")
    input("presione cualquier tecla para continuar.......")
def opcio6(cantidad):
    precio = 499
    precioFinal = precio * cantidad
    print(f"Precio a pagar: {precioFinal}")
    input("presione cualquier tecla para continuar.......")
def opcio7(cantidad):
    precio = 1000
    precioFinal = precio * cantidad
    print(f"Precio a pagar: {precioFinal}")
    input("presione cualquier tecla para continuar.......")
def otros():
    print("Opción no válida.")
    input("presione cualquier tecla para continuar.......")
opciones1 = {
    1: opcio1,
    2: opcio2,
    3: opcio3,
    4: opcio4,
    5: opcio5,
    6: opcio6,
    7: opcio7,
}
def list_opciones1(opcio, cantidad):
    return opciones1.get(opcio, otros)(cantidad)
def opcion1():
    while True:
        os.system("cls")
        try:    
            print("Compras")
            print("|----------------------------|")
            print("|     Selecione su compra    |")
            print("|----------------------------|")
            print("| 1. Tomate                  |")
            print("| 2. Apio                    |")
            print("| 3. Arroz                   |")
            print("| 4. Fideos                  |")
            print("| 5. Apio                    |")
            print("| 6. Mandarina               |")
            print("| 7. Pan                     |")
            print("| 8. Salir                   |")
            print("|----------------------------|")
            num = int(input("Seleccione su opcion: "))
            if num == 8:
                break
            cantidad = int(input("Ingrese la cantidad de lo que nesecita: "))
            list_opciones1(num, cantidad)

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
            continue
def opcion2():
    while True:
        os.system("cls")
        try:    
            print("Ventas")
            print("|-----------------------------------------------|")
            print("|     Selecione su lo que le gustaria vender    |")
            print("|-----------------------------------------------|")
            print("| 1. Tomate                                     |")
            print("| 2. Apio                                       |")
            print("| 3. Arroz                                      |")
            print("| 4. Fideos                                     |")
            print("| 5. Apio                                       |")
            print("| 6. Mandarina                                  |")
            print("| 7. Pan                                        |")
            print("| 8. Salir                                      |")
            print("|-----------------------------------------------|")
            opcion = int(input("Seleccione su opcion: "))
            if opcion == 8:
                break
            


        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
            continue
opciones_menu = {
    1: opcion1,
    2: opcion2

}
def list_opciones2(opcion):
    return opciones_menu.get(opcion, otros)()
def menu():
    while True:
        os.system("cls")
        try:    
            print("Venta de Producto")
            print("|------------------------------------|")
            print("|      Seleccione que va a hacer     |")
            print("|------------------------------------|")
            print("| 1. Comprar                         |")
            print("| 2. Vender                          |")
            print("| 3. Salir                           |")
            print("|------------------------------------|")
            opcion = int(input("Seleccione su opcion: "))
            if opcion == 3:
                break
            list_opciones2(opcion)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
            continue
menu()

    