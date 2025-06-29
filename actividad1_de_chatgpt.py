import random
numero_aleatorio = random.randint(1, 100)

while True:
    try:
        entrada = int(input("Adivina el número entre 1 y 100: "))
        intento = int(entrada)
        if entrada > 100:
            print("Ingrese un numero menos de 100")
            input("Presione cualquier tecla para continuar.....")
            continue
        elif entrada < 1:
            print("Ingrese un numero mayor que 1")
            input("Presione cualquier tecla para continuar.....")
            continue
        # Verificar si el número está fuera del rangos
        if intento < 1 or intento > 100:
            print("El número debe estar entre 1 y 100.")
            continue
        
        # Comparar el número ingresado con el número aleatorios
        if intento < numero_aleatorio:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_aleatorio:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print("¡Felicidades! Adivinaste el número.")
            break
    
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")
        input("Presione cualquier tecla para continuar.....")
