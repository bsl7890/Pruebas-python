"""" benjamin Santander
trabajo de POO sobre: Diseñar funciones y 
utilizar estructuras de control
4°E"""

import os  # Importa el módulo 'os' para usar funciones del sistema, como limpiar la pantalla

# 1) Función que evalúa si un número entero es mayor, menor o igual a 10
def evaluar_entero(x):
    if x > 10:
        print("El número es mayor que 10.")
    elif x < 10:
        print("El número es menor que 10.")
    else:
        print("El número es igual a 10.")

# 2) Función que evalúa si un número decimal es mayor, menor o igual a 10
def evaluar_decimal(x):
    if x > 10:
        print("El número es mayor que 10.")
    elif x < 10:
        print("El número es menor que 10.")
    else:
        print("El número es igual a 10.")

# 3) Función que calcula el área de un triángulo con base y altura
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2  # Fórmula para calcular el área
    print("El área del triángulo es:", area)

# 4) Función que saluda al usuario con su nombre y edad
def saludar(nombre, edad):
    print(f"Hola, {nombre}. Me alegra que tengas {edad} años.")
    input("presione cualquier tecla para continuar.......")  # Pausa

# 5) Función que suma varios números que el usuario ingresa
def sumar_numeros(cantidad):
    try:
        suma = 0
        for i in range(cantidad):  # Se repite según la cantidad indicada
            numero = float(input(f"Ingrese el número {i+1}: "))
            suma += numero  # Acumula la suma
        print("La suma total es:", suma)
    except ValueError:  # Maneja errores si el usuario no escribe un número
        print("Error: Ingresa solo números válidos.")

# ----------------------
# Llamadas de prueba
# ----------------------

# Solicita un número entero con validación
while True:
    os.system("cls")  # Limpia la pantalla
    try:
        numero = int(input("Ingresa un número entero: "))
        evaluar_entero(numero)
        input("presione cualquier tecla para continuar.......")
        break  # Sale del bucle si no hay error
    except ValueError:
        print("Error: Ingresa un número entero válido.")
        input("presione cualquier tecla para continuar.......")
        continue  # Repite el bucle si hay error

# Solicita un número decimal con validación
while True:
    os.system("cls")
    try:
        numero_decimal = float(input("Ingresa un número decimal: "))
        evaluar_decimal(numero_decimal)
        input("presione cualquier tecla para continuar.......")
        break
    except ValueError:
        print("Error: Ingresa un número decimal válido.")
        input("presione cualquier tecla para continuar.......")
        continue

# Solicita la base y la altura del triángulo con validación
while True:
    os.system("cls")
    try:
        base = int(input("Ingresa la base del triángulo: "))
        altura = int(input("Ingresa la altura del triángulo: "))
        calcular_area_triangulo(base, altura)
        input("presione cualquier tecla para continuar.......")
        break
    except ValueError:
        print("Error: Ingresa números enteros para base y altura.")
        input("presione cualquier tecla para continuar.......")
        continue

# Saludo personalizado
saludar("Benjamín", 18)

# Solicita cuántos números se quieren sumar con validación
while True:
    os.system("cls")
    try:
        cantidad = int(input("¿Cuántos números quieres sumar?: "))
        sumar_numeros(cantidad)
        input("presione cualquier tecla para continuar.......")
        break
    except ValueError:
        print("Error: Ingresa un número entero válido.")
        input("presione cualquier tecla para continuar.......")
        continue
