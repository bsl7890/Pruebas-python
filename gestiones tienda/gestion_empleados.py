import os
os.system("cls")
empleados = []
def op1():
    return "Gerente"
def op2():
    return "Ingeniero"
def op3():
    return "Administrador"
def op4():
    return "Desarrollador"
def op5():
    return "Asistente Administrativo"
def op6():
    return "Analista de Datos"
def op7():
    return "Diseñador Gráfico"
def op8():
    return "Especialista en Marketing"
def op9():
    return "Recursos Humanos"
def op10():
    return "Contador"
def op11():
    return "Técnico de Soporte"
def op12():
    return "Secretaria"
def op13():
    return "Jefe de Proyecto"
def op14():
    return "Vendedor"
def op15():
    return "Consultor"
def otros():
    return "Opción no válida"
opciones = {
    1: op1,
    2: op2,
    3: op3,
    4: op4,
    5: op5,
    6: op6,
    7: op7,
    8: op8,
    9: op9,
    10: op10,
    11: op11,
    12: op12,
    13: op13,
    14: op14,
    15: op15,
}
def opcione1(opcion):
    return opciones.get(opcion, otros)()

def opcion1():
    os.system("cls")
    print("Opcion 1 seleccionada: Ingresar sueldo base")
    while True:   
        try:
            nombre = input("Ingrese el nombre del empleado: ")
            edad = int(input("Ingrese la edad del empleado: "))
            salario = float(input("Ingrese el salario del empleado: "))
            if edad <= 0 and salario <= 0:
                print("La edad y el salario deben ser mayores a 0.")
                input("presione cualquier tecla para continuar.......")
                continue
            print("|-------------------------------------|")
            print("|         Seleccione su cargo         |")
            print("|-------------------------------------|")
            print("| 1. Gerente                          |")
            print("| 2. Ingeniero                        |")
            print("| 3. Administrador                    |")
            print("| 4. Desarrollador                    |")
            print("| 5. Asistente Administrativo         |")
            print("| 6. Analista de Datos                |")
            print("| 7. Diseñador Gráfico                |")
            print("| 8. Especialista en Marketing        |")
            print("| 9. Recursos Humanos                 |")
            print("| 10. Contador                        |")
            print("| 11. Técnico de Soporte              |")
            print("| 12. Secretaria                      |")
            print("| 13. Jefe de Proyecto                |")
            print("| 14. Vendedor                        |")
            print("| 15. Consultor                       |")
            print("|-------------------------------------|")
            cargo = int(input("Ingrese su opción: "))
            cargo_seleccionado = opcione1(cargo)
            if cargo_seleccionado == "Opción no válida":
                print("Opción no válida. Por favor, seleccione un cargo válido.")
                input("presione cualquier tecla para continuar.......")
                continue
            empleados.append({
                "nombre": nombre,
                "edad": edad,
                "cargo": cargo_seleccionado,
                "salario": salario
            })
            print("Empleado registrado con éxito.")
            print(f"\nNombre: {nombre}\nEdad: {edad}\nCargo: {cargo_seleccionado}\nSalario: {salario}")
            input("presione cualquier tecla para continuar.......")
            gestion_Empleados()
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
            continue

def opcion2():
    os.system("cls")
    print("Opcion 2 seleccionada: Ver lista de empleados")
    
    if not empleados:  # Si no hay empleados registrados
        print("No hay empleados registrados.")
    else:
        print("|-------------------------------------|")
        print("|         Lista de Empleados          |")
        print("|-------------------------------------|")
        for empleado in empleados:
            print(f"Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Cargo: {empleado['cargo']}, Salario: {empleado['salario']}")
    input("Presione cualquier tecla para continuar...")
    gestion_Empleados()

def opcion3():
    os.system("cls")
    print("Opcion 3 seleccionada: Buscar empleado")
    nombre_buscar = input("Ingrese el nombre del empleado a buscar: ")
    encontrado = False
    for empleado in empleados:
        if empleado["nombre"].lower() == nombre_buscar.lower():  # Comparar sin importar mayúsculas/minúsculas
            print(f"Empleado encontrado: {empleado}")
            encontrado = True
            gestion_Empleados()
    if not encontrado:
        print("Empleado no encontrado.")
    input("Presione cualquier tecla para continuar...")
def opcion4():
    os.system("cls")
    print("Opcion 4 seleccionada: Actualizar salario")
    nombre_buscar = input("Ingrese el nombre del empleado a buscar: ")
    encontrado = False
    for empleado in empleados:
        if empleado["nombre"].lower() == nombre_buscar.lower(): 
            try:
                salario_actualizar = float(input("Ingrese el nuevo salario: "))
                if salario_actualizar <= 0:
                    print("El salario debe ser mayor a 0.")
                    input("presione cualquier tecla para continuar.......")
                    return
                empleado["salario"] = salario_actualizar
                print(f"Salario actualizado a: {empleado['salario']}")
                print(f"Empleado actualizado: {empleado}")
                encontrado = True
                input("presione cualquier tecla para continuar.......")
                gestion_Empleados()
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
                input("presione cualquier tecla para continuar.......")
                return
    if not encontrado:
        print("Empleado no encontrado.")
def opcion5 ():
    print("Opcion 5 seleccionada: Salir")
    return "salir"
def otros1():
    return "Opción no válida"
opcione = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4,
    5: opcion5,
}
def opciones2(opcion1):
    return opcione.get(opcion1, otros1)()

def gestion_Empleados():
    while True:
        os.system("cls")
        try:
            print("Bienvenido a la gestión de empleados")
            print("|-------------------------------------|")
            print("|         Gestión de Empleados        |")
            print("|-------------------------------------|")
            print("| 1. Registrar nuevo empleado         |")
            print("| 2. Ver lista de empleados           |")
            print("| 3. Buscar empleado                  |")
            print("| 4. Actualizar salario               |")
            print("| 5. Salir                            |")
            print("|-------------------------------------|")
            opcion = int(input("Ingrese su opción: "))
            opcion_seleccionada = opciones2(opcion)
            if opcion_seleccionada == "salir":
                break
            elif opcion > 5:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                input("presione cualquier tecla para continuar.......")
                continue
            opcion_seleccionada() 
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
            continue

