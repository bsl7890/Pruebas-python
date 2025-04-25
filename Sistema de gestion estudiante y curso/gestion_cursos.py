import os
asignaturas = []
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

def opcion1():
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

            for cursos in asignaturas:
                if cursos["Asignatura"].lower() == curso.lower():
                    print(f"El curso '{curso}' ya está registrado.")
                    input("presione cualquier tecla para continuar.......")
                    break
            else:
                asignaturas.append({"Asignatura": curso})
                print(f"Curso '{curso}' agregado exitosamente.")
                input("presione cualquier tecla para continuar.......")
            menu_cursos()
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
            continue
def opcion2():
    print("Seleccionaste la opción 2: Ver todos los cursos")
    print("|----------------------------------------------|")
    print("|               Lista de cursos                |")
    print("|----------------------------------------------|")
    if not asignaturas:
        print("No hay cursos registrados.")
    else:
        for cursos in asignaturas:
            print(f"Curso: {cursos['Asignatura']}")
    print("|----------------------------------------------|")
    print("--------------------------------------------------")
    print("Total de cursos registrados:", len(asignaturas))
    print("--------------------------------------------------")
    input("presione cualquier tecla para continuar.......")
    menu_cursos()
def opcion3():
    while True:
        os.system("cls")
        try:        
            print("Seleccionaste la opción 3: Eliminar curso")
            print("|----------------------------------------------|")
            print("|               Lista de cursos                |")
            print("|----------------------------------------------|")
            for cursos in asignaturas:
                print(f"Curso: {cursos['Asignatura']}")
            print("|----------------------------------------------|")
            curso_eliminar = input("Ingrese el nombre del curso a eliminar: ")
            encontrado = False
            for cursos in asignaturas:
                if cursos["Asignatura"].lower() == curso_eliminar.lower():
                    confirmacion = input(f"¿Estás seguro de eliminar el curso '{cursos['Asignatura']}'? (s/n): ")
                    if confirmacion.lower() == "s":
                        asignaturas.remove(cursos)
                        print(f"Curso '{cursos['Asignatura']}' eliminado exitosamente.")
                        encontrado = True
                        break
                    elif confirmacion.lower() == "n":
                        print("Eliminación cancelada.")
                        encontrado = True
                        break
            if not encontrado:
                print(f"Curso '{curso_eliminar}' no encontrado.")
            input("presione cualquier tecla para continuar.......")
            menu_cursos()
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
            continue
def opcion4():
    while True:
        os.system("cls")
        try:
            print("Seleccionaste la opción 4: Buscar curso")
            print("|----------------------------------------------|")
            print("|               Lista de cursos                |")
            print("|----------------------------------------------|")
            for cursos in asignaturas:
                print(f"Curso: {cursos['Asignatura']}")
            print("|----------------------------------------------|")
            curso_buscar = input("Ingrese el nombre del curso a buscar: ")
            encontrado = False
            for cursos in asignaturas:
                if cursos["Asignatura"].lower() == curso_buscar.lower():
                    print(f"Curso encontrado: {cursos['Asignatura']}")
                    encontrado = True
                    break
            if not encontrado:
                print(f"Curso '{curso_buscar}' no encontrado.")
            input("presione cualquier tecla para continuar.......")
            menu_cursos()
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
            continue
def opcion5():
    while True:
        os.system("cls")
        try:
            print("Seleccionaste la opción 5: Actualizar curso")
            print("|----------------------------------------------|")
            print("|               Lista de cursos                |")
            print("|----------------------------------------------|")
            for cursos in asignaturas:
                print(f"Curso: {cursos['Asignatura']}")
            print("|----------------------------------------------|")
            curso_actualizar = input("Ingrese el nombre del curso a actualizar: ")
            encontrado = False
            for cursos in asignaturas:
                if cursos["Asignatura"].lower() == curso_actualizar.lower():
                    nuevo_curso = input("Ingrese el nuevo nombre del curso: ")
                    cursos["Asignatura"] = nuevo_curso
                    print(f"Curso actualizado a: {cursos['Asignatura']}")
                    encontrado = True
                    break
            if not encontrado:
                print(f"Curso '{curso_actualizar}' no encontrado.")
            input("presione cualquier tecla para continuar.......")
            menu_cursos()
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
            continue
def opcion6():
    print("Seleccionaste la opción 6: Salir")
    return "salir"
def otros():
    print("Opción no válida.")
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
def menu_cursos():
    while True:
        os.system("cls")
        try:
            print("Bienvenido a la gestión de estudiantes")
            print("|-------------------------------------|")
            print("|         Gestion de cursos           |")
            print("|-------------------------------------|")
            print("| 1. Agregar Agregar curso            |")
            print("| 2. Ver todos los cursos             |")
            print("| 3. Eliminar curso                   |")
            print("| 4. Buscar curso                     |")
            print("| 5. Actualizar curso                 |")
            print("| 6. Salir                            |")
            print("|-------------------------------------|")
            opcion = int(input("Ingrese su opción: "))
            opcion_seleccionada = list_opciones(opcion)
            if opcion_seleccionada == "salir":
                break
            if opcion < 1 or opcion > 6:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                input("presione cualquier tecla para continuar.......")
                continue
            list_opciones(opcion)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
            continue

