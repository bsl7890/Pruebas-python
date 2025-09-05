import gestion_empleados
import gestion_inventario
import os

def opcion1():
    return gestion_empleados.gestion_Empleados()
def opcion2():
    return gestion_inventario.menu_inventario()
def opcion3():
    print("Seleccionaste la opción 3: Salir")
    exit()
def otros():
    print("Opción no válida.")
    input("presione cualquier tecla para continuar.......")
opciones = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
}
def list_opciones(opcione):
    return opciones.get(opcione, otros)()

def menu_principal():
    while True:    
        os.system("cls")
        try:
            print("|------------------------------------------|")
            print("|          Menu Principal                  |")
            print("|------------------------------------------|")
            print("| 1. Gestionar Empleados                   |")
            print("| 2. Gestionar Inventario                  |")
            print("| 3. Salir                                 |")
            print("|------------------------------------------|")
            opcion = int(input("Seleccione una opción: "))
            list_opciones(opcion)
            if opcion > 3:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            continue

menu_principal()
