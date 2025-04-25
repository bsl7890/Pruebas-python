import os
estudiante =[]
def opcion1():
    print("Seleccionaste la opción 1: Agregar estudiante")
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    if edad <= 0:
        print("La edad debe ser mayor a 0.")
        input("presione cualquier tecla para continuar.......")
        return
    curso = input("Ingrese el curso del estudiante: ")
    estudiante.append({"nombre": nombre,"edad": edad,"curso": curso})
    print(f"Estudiante registrado: {estudiante}")
    input("presione cualquier tecla para continuar.......")
    gestion_Empleados()
def opcion2():
    print("Seleccionaste la opción 2: Ver todos los estudiantes")
    if not estudiante:
        print("No hay estudiantes registrados.")
    else:
        print("|-------------------------------------|")
        print("|         Lista de Estudiantes        |")
        print("|-------------------------------------|")
        for est in estudiante:
            print(f"Nombre: {est['nombre']}\nEdad: {est['edad']}\nCurso: {est['curso']}")
            print("--------------------------------------------------")
    print("--------------------------------------------------")
    print("Total de estudiantes registrados:", len(estudiante))
    input("presione cualquier tecla para continuar.......")
    gestion_Empleados()
def opcion3():
    print("Seleccionaste la opción 3: Eliminar estudiante por nombre")
    nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
    curso = input("Ingrese el curso del estudiante a buscar: ")
    encontrado = False
    for estudiantes in estudiante:
        if estudiantes["nombre"].lower() == nombre_buscar.lower() and estudiantes["curso"].lower() == curso.lower():
            print(f"Estudiante encontrado: {estudiantes}")
            estudiante.remove(estudiantes)
            print(f"Estudiante {nombre_buscar} del curso {curso} eliminado.")
            encontrado = True
            break
    if not encontrado:
        print("Estudiante no encontrado.")
    input("presione cualquier tecla para continuar.......")
    gestion_Empleados()
def opcion4():
    print("Seleccionaste la opción 4: Buscar estudiante por nombre")
    nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
    encontrado = False
    for estudiantes in estudiante:
        if estudiantes["nombre"].lower() == nombre_buscar.lower():
            print(f"Estudiante encontrado: {estudiantes}")
            encontrado = True
            break
    if not encontrado:
        print("Estudiante no encontrado.")
    input("presione cualquier tecla para continuar.......")
    gestion_Empleados()
def opcion5():
    print("Seleccionaste la opción 5: Actualizar estudiante")
    nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
    curso = input("Ingrese el curso del estudiante a buscar: ")
    encontrado = False
    for estudiantes in estudiante:
        if estudiantes["nombre"].lower() == nombre_buscar.lower() and estudiantes["curso"].lower() == curso.lower():
            print(f"Estudiante encontrado: {estudiantes}")
            nuevo_nombre = input("Ingrese el nuevo nombre del estudiante: ")
            nueva_edad = int(input("Ingrese la nueva edad del estudiante: "))
            nuevo_curso = input("Ingrese el nuevo curso del estudiante: ")
            estudiantes["nombre"] = nuevo_nombre
            estudiantes["edad"] = nueva_edad
            estudiantes["curso"] = nuevo_curso
            print(f"Estudiante actualizado: {estudiantes}")
            encontrado = True
            break
    if not encontrado:
        print("Estudiante no encontrado.")
    input("presione cualquier tecla para continuar.......")
    gestion_Empleados()
def opcion6():
    print("Seleccionaste la opción 6: Salir")
    return "salir"
def otros():
    print("Opción no válida. Por favor, seleccione una opción válida.")
    input("presione cualquier tecla para continuar.......")
opciones = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4,
    5: opcion5,
    6: opcion6
}

def list_opciones(opcion):
    return opciones.get(opcion, otros)()

def gestion_Empleados():
    while True:
        os.system("cls")
        try:
            print("Bienvenido a la gestión de estudiantes")
            print("|-------------------------------------|")
            print("|         Gestion de estudiantes      |")
            print("|-------------------------------------|")
            print("| 1. Agregar estudiante               |")
            print("| 2. Ver todos los estudiantes        |")
            print("| 3. Eliminar estudiante              |")
            print("| 4. Buscar estudiante                |")
            print("| 5. Actualizar estudiante            |")
            print("| 6. Salir                            |")
            print("|-------------------------------------|")
            opcion = int(int(input("Ingrese su opción: ")))
            opcion_seleccionada = list_opciones(opcion)
            if opcion_seleccionada == "salir":
                break
            if opcion < 1 or opcion > 6:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                input("presione cualquier tecla para continuar.......")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
            continue