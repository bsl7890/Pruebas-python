import os

def limpiar_pantalla():
    os.system("cls")

def opcion1():
    global sueldoBase
    try:
        sueldoBase = int(input("Ingrese el nuevo sueldo base: "))
        return input(f"Sueldo base actualizado a: {sueldoBase}\nPresione cualquier tecla para continuar.....")
    except ValueError:
        return input("Entrada no válida. Por favor, ingrese un número.\nPresione cualquier tecla para continuar.....")

def opcion2():
    MenuDeducciones()

def opcion3():
    MenuBonificacion()

def opcion4():
    ValorNeto()

def otros():
    return "Opción no válida"

opciones = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4,
}

def opcio1(opciones1):
    return opciones.get(opciones1, otros)()

def Menu_Opciones():
    while True:
        limpiar_pantalla()
        try:
            print('======================================================')
            print("|          >>Menu de Opciones<<                        |")
            print('|    1. Ingresar sueldo base                           |')
            print('|    2. Aplicar deducciones                            |')
            print('|    3. Agregar bonificaciones                         |')
            print('|    4. Calcular sueldo neto                           |')
            print('|    5. Salir                                          |')
            print('======================================================')
            Menu = int(input(""))
            opcion_seleccionada = opcio1(Menu)
            if Menu == 5:
                exit()
            elif Menu > 5:
                print(opcion_seleccionada)
                input("presione cualquier tecla para continuar.......")
                continue
        except ValueError:
            print(otros())  # Mostrar el mensaje de otros() en caso de error.
            input("presione cualquier tecla para continuar.......")

def MenuDeducciones():
    while True:
        limpiar_pantalla()
        try:
            print('======================================================')
            print("|          >>Menu de Deducciones<<                     |")
            print('|    1. AFP (10%)                                      |')
            print('|    2. Salud (7%)                                     |')
            print('|    3. Impuesto a la renta                            |')
            print('|    4. Volver                                         |')
            print('======================================================')
            Menu = int(input(""))

            if Menu == 4:
                return
            elif Menu == 1:
                AFP = 0.10
                SueldoAFP = sueldoBase * AFP
                print(f"Su sueldo AFP es {SueldoAFP:.2f}")
                input("presione cualquier tecla para continuar.......")
            elif Menu == 2:
                Salud = 0.07
                SueldoSalud = sueldoBase * Salud
                print(f"Su sueldo Salud es {SueldoSalud:.2f}")
                input("presione cualquier tecla para continuar.......")
            elif Menu == 3:
                AFP = 0.10
                Salud = 0.07
                SueldoAFP = sueldoBase * AFP
                SueldoSalud = sueldoBase * Salud
                Sueldoimponible = sueldoBase - SueldoAFP - SueldoSalud
                print(f"Su sueldo Imponible es {Sueldoimponible:.2f}")
                input("presione cualquier tecla para continuar.......")                
            else:
                print("Opción no válida.")
                input("Presione enter para continuar...")

        except ValueError:
            print("Por favor seleccione una de las opciones")
            input("presione cualquier tecla para continuar.......")

def MenuBonificacion():
    while True:
        limpiar_pantalla()
        try:
            print('======================================================')
            print("|          >>Menu de Deducciones<<                     |")
            print('|    1. Bono de productividad (+5%)                    |')
            print('|    2. Bono de transporte (+3%)                       |')
            print('|    3. Volver                                         |')
            print('======================================================')
            Menu = int(input(""))

            if Menu == 3:
                return
            elif Menu == 1:
                Productividad = 0.05
                BonoProductividad = sueldoBase * Productividad
                print(f"Su bono de Productividad es {BonoProductividad:.2f}")
                input("presione cualquier tecla para continuar.......")
            elif Menu == 2:
                Transporte = 0.03
                BonoTransporte = sueldoBase * Transporte
                print(f"Su bono Transporte es {BonoTransporte:.2f}")
                input("presione cualquier tecla para continuar.......")
            else:
                print("Opción no válida.")
                input("Presione enter para continuar...")
        except ValueError:
            print("Por favor seleccione una de las opciones")
            input("presione cualquier tecla para continuar.......")

def ValorNeto():
    while True:
        limpiar_pantalla()
        try:
            print('======================================================')
            print("|          >>Menu de Deducciones<<                     |")
            print('|    1. Calcular valor neto                            |')
            print('|    2. Volver                                         |')
            print('======================================================')
            Menu = int(input(""))

            if Menu == 2:
                return
            elif Menu == 1:
                iva = 0.19
                Productividad = 0.05
                Transporte = 0.03
                AFP = 0.10
                Salud = 0.07
                SueldoSalud = sueldoBase * Salud
                SueldoAFP = sueldoBase * AFP
                Sueldoimponible = sueldoBase - SueldoAFP - SueldoSalud
                BonoTransporte = sueldoBase * Transporte
                BonoProductividad = sueldoBase * Productividad
                valorIva = sueldoBase * iva
                valorbruto = sueldoBase + valorIva
                descuentos = SueldoAFP + SueldoSalud
                bonificacion = BonoProductividad + BonoTransporte
                ValorNeto = valorbruto + bonificacion - descuentos
                print(f"el valor neto es: {ValorNeto:.2f}")
                input("presione cualquier tecla para continuar.......")
        except ValueError:
            print("Por favor seleccione una de las opciones")
            input("presione cualquier tecla para continuar.......")

while True:
    os.system("cls")
    try:
        sueldoBase = int(input("Ingrese su sueldo base: "))
        Menu_Opciones()
    except ValueError:
        print("Opción no válida")  # Mostrar el mensaje de otros() en caso de error.
        input("presione cualquier tecla para continuar.......")
