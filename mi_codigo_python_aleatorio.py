import os

def opcion1():
    print("Opcion 1 seleccionada: Sumar dos numeros")
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")

def opcion2():
    print("Opcion 2 seleccionada: Restar dos numeros")
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")

def opcion3():
    print("Opcion 3 seleccionada: Multiplicar dos numeros")
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    resultado = num1 * num2
    print(f"El resultado de la multiplicacion es: {resultado}")

def opcion4():
    print("Opcion 4 seleccionada: Dividir dos numeros")
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        resultado = num1 / num2
        print(f"El resultado de la division es: {resultado}")

def opcion5():
    menubonificacion()

def opcion7():
    print("Saliendo del programa...")
    exit()

def otros():
    print("Opcion no valida. Por favor, seleccione una opcion valida.")

opciones = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4,
    5: opcion5,
}

def opcione1(opcion):
    return opciones.get(opcion, otros)()

def opcio1():
    return "Trabajador"
def opcio2():
    return "Estudiante"
def opcio3():
    return "Becario"
def opcio4():
    return "Salir"

opciones1 = {
    1: opcio1,
    2: opcio2,
    3: opcio3,
    4: opcio4,
}

def opcione2(opcion):
    return opciones1.get(opcion, otros)()

def menubonificacion():
    while True:
        os.system("cls")
        try:
            print("Opcion 5 seleccionada: Agregar bonificaciones")
            edad = int(input("Ingrese su edad: "))
            salario = float(input("Ingrese su salario: "))
            if edad <= 18:
                bonificacion = salario * 0.10
            elif 19 <= edad <= 30:
                bonificacion = salario * 0.15
            elif edad > 30:
                bonificacion = salario * 0.20
            else:
                bonificacion = 0
            print(f"Su bonificacion es: {bonificacion}")
            
            print("|------------------------------------|")
            print("|         Seleccione una opcion      |")
            print("|------------------------------------|")
            print("| 1. Trabajador                      |")
            print("| 2. Estudiante                      |")
            print("| 3. Becario                         |")
            print("| 4. Salir                           |")
            print("|------------------------------------|")
            opcion = int(input("Ingrese su opcion: "))
            opcion_seleccionada = opcione2(opcion)
            
            if opcion_seleccionada == "Trabajador":
                print("Usted es un trabajador")
                salario += bonificacion
                print(f"Su nuevo salario es: {salario}")
                input("presione cualquier tecla para continuar.......")
                menu()
            elif opcion_seleccionada == "Estudiante":
                print("Usted es un estudiante")
                salario += bonificacion
                print(f"Su nuevo salario es: {salario}")
                input("presione cualquier tecla para continuar.......")
                menu()
            elif opcion_seleccionada == "Becario":
                print("Usted es un becario")
                salario += bonificacion
                print(f"Su nuevo salario es: {salario}")
                input("presione cualquier tecla para continuar.......")
                menu()
            elif opcion_seleccionada == "Salir":
                print("Saliendo del programa...")
                menu()
            else:
                print(otros())
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("presione cualquier tecla para continuar.......")
def menu():
    while True:
        os.system("cls")
        try:
            print("|------------------------------------|")
            print("|         Seleccione una opcion      |")
            print("|------------------------------------|")
            print("| 1. Sumar dos numeros               |")
            print("| 2. Restar dos numeros              |")
            print("| 3. Multiplicar dos numeros         |")
            print("| 4. Dividir dos numeros             |")
            print("| 5. Menu bonificaciones             |")
            print("| 6. Menu deducciones                |")
            print("| 7. Salir                           |")
            print("|------------------------------------|")
            opcion = int(input("Ingrese su opcion: "))
            opcion_seleccionada = opcione1(opcion)
            if opcion == 5:
                break
            elif opcion > 5:
                print(opcion_seleccionada)
                input("presione cualquier tecla para continuar.......")
                continue
            else:
                input("presione cualquier tecla para continuar.......")
        except ValueError:
            print(otros())
            input("presione cualquier tecla para continuar.......")

menu()
