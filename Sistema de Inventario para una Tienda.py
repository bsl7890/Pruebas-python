import os
os.system("cls" if os.name == "nt" else "clear")
productos = []
def opcion1():
    print("Seleccionaste la opción 1: Agregar nuevo producto")
    nombre_producto = input("Ingrese el nombre del producto: ")
    while True:
        try:
            cantidad_producto = int(input("Ingrese la cantidad del producto: "))
            if cantidad_producto <= 0:
                print("La cantidad debe de ser mayor que 0.")
                input("presione cualquier tecla para continuar.......")
                return
            precio_producto = float(input("Ingrese el precio del producto: "))
            if precio_producto <= 0:
                print("El precio debe de ser mayor que 0.")
                input("presione cualquier tecla para continuar.......")
                return
            productos.append({
                "nombre": nombre_producto,
                "cantidad": cantidad_producto,
                "precio": precio_producto
            })
            print(f"Productos registrados: {productos}")
            input("presione cualquier tecla para continuar.......")
            return
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
            return
def opcion2():
    print("Seleccionaste la opción 2: Ver todos los productos")
    if not productos:
        print("No hay productos registrados.")
    else:
        for producto in productos:
            print(f"1. Nombre: {producto['nombre']}\n2. Cantidad: {producto['cantidad']}\n3. Precio: {producto['precio']}")
    input("presione cualquier tecla para continuar.......")
def opcion3():
    print("Seleccionaste la opción 3: Buscar producto por nombre")
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print(f"Producto encontrado: {producto}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")
    input("presione cualquier tecla para continuar.......")
def opcion4():
    print("Seleccionaste la opción 4: Actualizar cantidad de un producto")
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            while True:
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    if nueva_cantidad <= 0:
                        print("La cantidad debe de ser mayor que 0.")
                        input("Presione cualquier tecla para continuar.......")
                        return
                    producto["cantidad"] = nueva_cantidad
                    print(f"Cantidad actualizada a: {producto['cantidad']}")
                    print(f"Producto actualizado: {producto}")
                    encontrado = True
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")
                    input("presione cualquier tecla para continuar.......")
                    return
    if not encontrado:
        print("Producto no encontrado.")
def opcion5():
    print("Seleccionaste la opcion 5: Eliminar producto")
    nombre_buscar = input("Ingrese el nombre del producto a eliminar: ")
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            productos.remove(producto)
            print(f"Producto eliminado: {producto}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")
    input("presione cualquier tecla para continuar.......")
def opcion6():
    print("Seleccionaste la opción 6: Salir")
    exit()
def otros():
    return "Opción no válida"
opciones = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4,
    5: opcion5,
    6: opcion6,
}
def list_opciones(opcione):
    return opciones.get(opcione, otros)()


def menu_inventario():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        try:
            print("|------------------------------------------|")
            print("|          Sistema de Inventario           |")
            print("|------------------------------------------|")
            print("| 1. Agregar nuevo producto                |")
            print("| 2. Ver todos los productos               |")
            print("| 3. Buscar producto por nombre            |")
            print("| 4. Actualizar cantidad de un producto    |")
            print("| 5. Eliminar producto                     |")
            print("| 6. Salir                                 |")
            print("|------------------------------------------|")
            opcion = int(input("Ingrese su opción: "))
            list_opciones(opcion)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
            return

menu_inventario()

