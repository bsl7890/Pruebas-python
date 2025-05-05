"""" benjamin Santader
trabajo de POO sobre una Diseñar funciones y 
utilizar estructuras de control
4°E"""
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

# 3) Función que calcula el área de un triángulo
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    print("El área del triángulo es:", area)

# 4) Función que recibe nombre y edad, y muestra un mensaje
def saludar(nombre, edad):
    print(f"Hola, {nombre}. Me alegra que tengas {edad} años.")

# 5) Función que suma una cantidad definida de números ingresados por el usuario
def sumar_numeros(cantidad):
    try:
        suma = 0
        for i in range(cantidad):
            numero = float(input(f"Ingrese el número {i+1}: "))
            suma += numero
        print("La suma total es:", suma)
    except ValueError:
        print("Error: Ingresa solo números válidos.")

# ----------------------
# Llamadas de prueba
# ----------------------

try:
    numero = int(input("Ingresa un número entero: "))
    evaluar_entero(numero)
except ValueError:
    print("Error: Ingresa un número entero válido.")

try:
    numero_decimal = float(input("Ingresa un número decimal: "))
    evaluar_decimal(numero_decimal)
except ValueError:
    print("Error: Ingresa un número decimal válido.")

try:
    base = int(input("Ingresa la base del triángulo: "))
    altura = int(input("Ingresa la altura del triángulo: "))
    calcular_area_triangulo(base, altura)
except ValueError:
    print("Error: Ingresa números enteros para base y altura.")

saludar("Benjamín", 17)

try:
    cantidad = int(input("¿Cuántos números quieres sumar?: "))
    sumar_numeros(cantidad)
except ValueError:
    print("Error: Ingresa un número entero válido.")
