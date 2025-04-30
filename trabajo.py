def evaluar_numero(x):
    try:
        if x > 10:
            mensaje = "El número es mayor que 10."
        elif x < 10:
            mensaje = "El número es menor que 10."
        else:
            mensaje = "El número es igual a 10."
        return mensaje
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")
        return "Error"
numero = int(input("Ingresa un número entero: "))
print(evaluar_numero(numero))

def evaluar_decimal(x):
    try:
        if x > 10:
            mensaje = "El número es mayor que 10."
        elif x < 10:
            mensaje = "El número es menor que 10."
        else:
            mensaje = "El número es igual a 10."
            
        return mensaje
    
    except ValueError:
        print("Error: Debes ingresar un número decimal válido (usa punto, no coma).")
        return "Error"

numero_decimal = float(input("Ingresa un número con decimales (indicar el decimal con '.'):  "))
print(evaluar_decimal(numero_decimal))

def area_triangulo(a,b):
    return a*b/2

base = int(input("Ingrese un numero entero para la base del triangulo: "))
altura = int(input("Ingrese un numero entero para la altura del triangulo: "))
print(area_triangulo(base, altura))

def nombre_edad(nombre,edad):
    return f"Hola, {nombre}. Me alegra que tengas {edad} años"

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print(nombre_edad(nombre, edad))

def sumar_numeros(x):
    try:

        for i in range(x):
            numero = float(input(f"Ingrese el número: "))
            numeros.append(numero)

        resultado = sum(numeros)
        print("La suma total es:", resultado)
        return resultado

    except ValueError:
        print("Error: debes ingresar solo números válidos.")
        return None
cantidad = int(input("¿Cuántos números quieres sumar? "))
numeros = []

print(sumar_numeros())
