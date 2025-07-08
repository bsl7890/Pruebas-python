import os

cursos = []
def opcio1():
    return "Programacion"
def opcio2():
    return "Diseño de software"
def opcio3():
    return "Desarrollo web"
def opcio4():
    return "Desarrollo de aplicaciones moviles"
def opcio5():
    return "Desarrollo de videojuegos"
def opcio6():
    return "Inteligencia artificial"
def opcio7():
    return "Ciencia de datos"
def opcio8():
    return "Big data"
def opcio9():
    return "Ciberseguridad"
def opcio10():
    return "Matematicas"
def opcio11():
    return "Fisica"
def opcio12():
    return "Quimica"
def opcio13():
    return "Biologia"
def opcio14():
    return "Historia"
def opcio15():
    return "Geografia"
def opcio16():
    return "Filosofia"
def opcio17():
    return "Psicologia"
def opcio18():
    return "Sociologia"
def opcio19():
    return "Economia"
def opcio20():
    return "Politica"
def opcio21():
    return "Derecho"
def opcio22():
    return "Antropologia"
def opcio23():
    return "Arqueologia"
def opcio24():
    return "Lingüística"
def opcio25():
    return "Literatura"
def opcio26():
    return "Arte"
def opcio27():
    return "Musica"
def opcio28():
    return "Danza"
def opcio29():
    return "Teatro"
def opcio30():
    return "Cine"
def opcio31():
    return "Fotografia"
def opcio32():
    return "Escultura"
def opcio33():
    return "Pintura"
def opcio34():
    return "Dibujo"
def opcio35():
    return "Emprendimiento"
def opcio36():
    return "Marketing"
def opcio37():
    return "Ventas"
def opcio38():
    return "Finanzas"
def opcio39():
    return "Contabilidad"
def opcio40():
    return "Recursos humanos"
def opcio41():
    return "Administracion"
def opcio42():
    return "Logistica"
def otros() :
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
    8: opcio8,
    9: opcio9,
    10: opcio10,
    11: opcio11,
    12: opcio12,
    13: opcio13,
    14: opcio14,
    15: opcio15,
    16: opcio16,
    17: opcio17,
    18: opcio18,
    19: opcio19,
    20: opcio20,
    21: opcio21,
    22: opcio22,
    23: opcio23,
    24: opcio24,
    25: opcio25,
    26: opcio26,
    27: opcio27,
    28: opcio28,
    29: opcio29,
    30: opcio30,
    31: opcio31,
    32: opcio32,
    33: opcio33,
    34: opcio34,
    35: opcio35,
    36: opcio36,
    37: opcio37,
    38: opcio38,
    39: opcio39,
    40: opcio40,
    41: opcio41,
    42: opcio42,
}

def list_opciones1(opcio):
    return opciones1.get(opcio, otros)()

def Agregar_curso():
    while True:
        os.system("cls")
        try:
            
            print("Seleccionaste la opción 1: Agregar curso")
            print("|----------------------------------------------|")
            print("|    Seleccione los cursos que desea agregar:  |")
            print("|----------------------------------------------|")
            print("| 1. Programacion                              |")
            print("| 2. Diseño de software                        |")
            print("| 3. Desarrollo web                            |")
            print("| 4. Desarrollo de aplicaciones moviles        |")
            print("| 5. Desarrollo de videojuegos                 |")
            print("| 6. Inteligencia artificial                   |")
            print("| 7. Ciencia de datos                          |")
            print("| 8. Big data                                  |")
            print("| 9. Ciberseguridad                            |")
            print("| 10. Matematicas                              |")
            print("| 11. Fisica                                   |")
            print("| 12. Quimica                                  |")
            print("| 13. Biologia                                 |")
            print("| 14. Historia                                 |")
            print("| 15. Geografia                                |")
            print("| 16. Filosofia                                |")
            print("| 17. Psicologia                               |")
            print("| 18. Sociologia                               |")
            print("| 19. Economia                                 |")
            print("| 20. Politica                                 |")
            print("| 21. Derecho                                  |")
            print("| 22. Antropologia                             |")
            print("| 23. Arqueologia                              |")
            print("| 24. Lingüística                              |")
            print("| 25. Literatura                               |")
            print("| 26. Arte                                     |")
            print("| 27. Musica                                   |")
            print("| 28. Danza                                    |")
            print("| 29. Teatro                                   |")
            print("| 30. Cine                                     |")
            print("| 31. Fotografia                               |")
            print("| 32. Escultura                                |")
            print("| 33. Pintura                                  |")
            print("| 34. Dibujo                                   |")
            print("| 35. Emprendimiento                           |")
            print("| 36. Marketing                                |")
            print("| 37. Ventas                                   |")
            print("| 38. Finanzas                                 |")
            print("| 39. Contabilidad                             |")
            print("| 40. Recursos humanos                         |")
            print("| 41. Administracion                           |")
            print("| 42. Logistica                                |")
            print("|----------------------------------------------|")
            opcionees1 = int(input("Ingrese su opción: "))
            curso = list_opciones1(opcionees1)
            if opcionees1 < 1 or opcionees1 > 42:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                input("presione cualquier tecla para continuar.......")
                continue
            for curso in cursos:
                if cursos["Asignatura"].lower() == curso.lower():
                    print(f"El curso '{curso}' ya está registrado.")
                    input("presione cualquier tecla para continuar.......")
                    break
            else:
                cursos.append({"Asignatura": curso})
                print(f"Curso '{curso}' agregado exitosamente.")
                input("presione cualquier tecla para continuar.......")
            Menú_Principal()
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
            continue
def agregar_alumno():
    while True:
        try:
            print("Seleccionaste la opción 2: Agregar alumno a un curso")
            alumno_ingresar = input("Ingrese el nombre del alumno: ")
            edad_alumno = int(input("Ingrese la edad del alumno"))
            if edad_alumno > 1:
                print("la edad no puede ser 0")
                input("presione cualquier tecla para continuar.......")
                continue
            print("|----------------------------------------------|")
            print("|               Lista de cursos                |")
            print("|----------------------------------------------|")
            if not cursos:
                print("No hay cursos registrados.")
            else:
                for curso in cursos:
                    print(f"Curso: {curso['Asignatura']}")
            curso_ingresar = input("Seleccione el curso a ingresar")
            curso_alumno = list_opciones1(curso_ingresar)
            for curso in cursos:
                if cursos["Asignatura"].lower() == curso_alumno.lower():
                    cursos.append({"nombre": alumno_ingresar, "edad": edad_alumno})
                else:
                    print("El curso aun no esta registrado en el sistema Por favor intente denuevo con otro curso")
                    input("presione cualquier tecla para continuar.......")
                    continue                    
        except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
                continue


def ver_cursos():
def opcion1():
    return Agregar_curso()
def opcion2():
    return agregar_alumno()


def Menú_Principal():
    while True:
        os.system("cls")
        try:
            os.system("cls")
            print("=== MENÚ PRINCIPAL ===")
            print("1. Agregar curso")
            print("2. Agregar alumno a un curso")
            print("3. Ver cursos y sus alumnos")
            print("4. Eliminar curso")
            print("5. Eliminar alumno de un curso")
            print("6. Buscar alumno por nombre")
            print("7. Salir")
            opcion = input("Selecciona una opción: ")
            opcion_selecionnada = ""
            if opcion == "7":
                print("Saliendo del sistema...")
                break
            else:
                input("Opción inválida. Presiona ENTER para continuar.")
        except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
                continue
