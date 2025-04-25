import gestion_estudiantes
import gestion_cursos
import matriculas
import os

def opcion1():
    return gestion_estudiantes.gestion_Empleados()
def opcion2():
    return gestion_cursos.menu_cursos()
def opcion3():
    return matriculas.menu_matricula()
def opcion4():
    print("Seleccionaste la opción 4: Salir")
    return "salir"
def otros():
    print("Opción no válida.")
    input("presione cualquier tecla para continuar.......")

opciones = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4,
}
def list_opciones(opcion):
    return opciones.get(opcion, otros)()

def menu_principal():
    while True:
        os.system("cls")
        try:
            print("|-------------------------------------------------|")
            print("|         Sistema de Gestión de Estudiantes       |")
            print("|-------------------------------------------------|")
            print("| 1. Gestionar Estudiantes                        |")
            print("| 2. Gestionar Cursos                             |")
            print("| 3. Gestionar Matrículas                         |")
            print("| 4. Salir                                        |")
            print("|-------------------------------------------------|")
            opcion = int(input("Seleccione una opción: "))
            opcionseleccionada = list_opciones(opcion)
            list_opciones(opcion)
            if opcionseleccionada == "salir":
                break
            if opcion< 1 or opcion > 4:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")

menu_principal()