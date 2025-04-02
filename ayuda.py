def opc1():
    return "Opción 1"

def opc2():
    return "Opción 2"

def opc3():
    return "Opción 3"

def opc4():
    return "Opción 4"

def otros():
    return "Opción no válida"

# Diccionario de opciones
opciones = {
    1: opc1,
    2: opc2,
    3: opc3,
    4: opc4
}

# Función que ejecuta la opción y retorna el resultado
def opcion(opc):
    return opciones.get(opc, otros)()  # Devuelve la ejecución de la función correcta o "otros"


while True:
    try:
        seleccion = input("Selecciona una opción (1, 2, 3, 4, o 'q' para salir): ")
        
        if seleccion.lower() == 'q':  # Permitir salir con 'q'
            print("Saliendo del programa...")
            break
        
        opcion_seleccionada = int(seleccion)  # Convertir entrada a número entero
        print(opcion(opcion_seleccionada))  # Imprimir el resultado

    except ValueError:  # Captura errores si ingresan algo que no es un número ni 'q'
        print("Por favor, ingresa un número válido.")
