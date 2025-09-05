import gestion_cursos
import gestion_estudiantes
import os
matricula = []
def opcion1():
    print("Seleccionaste la opción 1: Matricular estudiante en un curso")
    print("Lista de estudiantes disponibles:")
    for estudiantes in gestion_estudiantes.estudiante:
        print(f"Nombre: {estudiantes['nombre']}, Edad: {estudiantes['edad']}, Curso: {estudiantes['curso']}")
    print("Lista de asignaturas disponibles:")
    for curso in gestion_cursos.asignaturas:
        print(f"Asignatura: {curso['Asignatura']}, Horario: {curso['Horario']}, Docente: {curso['Docente']}")
    print("--------------------------------------------------")
    print("Total de estudiantes registrados:", len(gestion_estudiantes.estudiante))
    print("Total de asignaturas registradas:", len(gestion_cursos.asignaturas))
    print("--------------------------------------------------")
    print("Seleccione el estudiante que desea matricular en un curso.")
    print("--------------------------------------------------")
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    encontrado = False
    for estudiantes in gestion_estudiantes.estudiante:
        if estudiantes["nombre"].lower() == nombre_estudiante.lower():
            print(f"Estudiante encontrado: {estudiantes}")
            asignatura_elegida = input("Ingrese el nombre de la asignatura: ")
            encontrado_asignatura = False
            for curso in gestion_cursos.asignaturas:
                if curso["Asignatura"].lower() == asignatura_elegida.lower():
                    print(f"Asignatura encontrada: {curso}")
                    matricula.append({"Nombre": estudiantes["nombre"], "Asignatura": curso["Asignatura"]})
                    print(f"Estudiante {estudiantes['nombre']} matriculado en la asignatura {curso['Asignatura']}")
                    encontrado_asignatura = True
                    break

            if not encontrado_asignatura:
                print("Asignatura no encontrada.")
                input("presione cualquier tecla para continuar.......")
            encontrado = True
            break
    if not encontrado:
        print("Estudiante no encontrado.")
        input("presione cualquier tecla para continuar.......")
        return  
def opcion2():
    print("Seleccionaste la opción 2: Ver matrículas de un estudiante")
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    encontrado = False
    for estudiantes in matricula:
        if estudiantes["Nombre"].lower() == nombre_estudiante.lower():
            print(f"Estudiante encontrado: {estudiantes}")
            encontrado = True
            break
    if not encontrado:
        print("Estudiante no encontrado.")
    input("presione cualquier tecla para continuar.......")
    return
def opcion3():
    print("Seleccionaste la opción 3: Salir")
    return "salir"
def otros():
    print("Opción no válida.")
    input("presione cualquier tecla para continuar.......")
opciones = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
}
def list_opciones(opcion):
    return opciones.get(opcion, otros)()
def menu_matricula():
    while True:
        os.system("cls")
        try:
            print("|-------------------------------------------------|")
            print("|         Sistema de Gestión de Matrículas        |")
            print("|-------------------------------------------------|")
            print("| 1. Matricular estudiante en un curso            |")
            print("| 2. Ver Ver matrículas de un estudiante          |")
            print("| 3. Salir                                        |")
            print("|-------------------------------------------------|")
            opcion = int(input("Ingrese su opción: "))
            opcionseleccionada = list_opciones(opcion)
            list_opciones(opcion)
            if opcionseleccionada == "salir":
                break
            if opcion > 3:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                input("presione cualquier tecla para continuar.......")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
            continue
