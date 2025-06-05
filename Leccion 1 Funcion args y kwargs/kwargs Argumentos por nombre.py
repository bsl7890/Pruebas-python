# Esta función acepta argumentos con nombre, como nombre="Benjamín", edad=18, etc.
# Los convierte en un diccionario llamado "datos".
def mostrar_info(**datos):  
    # .items() convierte el diccionario en una lista de pares (clave, valor)
    # Ejemplo: {"nombre": "Benjamín"} → ("nombre", "Benjamín")
    for clave, valor in datos.items():  
        print(f"{clave}: {valor}")  # Muestra cada clave con su valor

# Llamamos a la función con 3 datos nombrados
mostrar_info(nombre="Benjamín", edad=18, curso="4° Medio", ciudad = "Santiago")
# 👉 Imprime:
# nombre: Benjamín
# edad: 18
# curso: 4° Medio
# ciudad: Santiago
def saludar(**kwargs):
    if "nombre" in kwargs:
        print(f"Hola, {kwargs['nombre']}!")
    else:
        print("Hola, desconocido")
    if "edad" in kwargs:
        print(f"Tienes {kwargs['edad']} años.")

saludar(nombre = "Martin")
saludar(nombre = "Alonso", edad = 17)
saludar()


def mostrar(*args, **kwargs):
	print("Posicionales: ", args)
	print("Nombrados: ", kwargs)

mostrar(1, 2, 3, nombre ="Yetzibel", edad = 18)


def mostrar_frutas(*frutas, **detalles):
    print("=== Lista de frutas ===")
    for fruta in frutas:
        print(f"- {fruta}")
    print("\n=== Detalles adicionales ===")
    for clave, valor in detalles.items():
        print(f"{clave}: {valor}")
mostrar_frutas("Manzana", "plátanos", "Naranja", color_favorito="Rojo", cantidad = 3, estacion = "Verano")



# Aplicar la funciones kwargs

# la funcion **kwargs se utiliza para pasar un numero variable de argumentos de 
# palabras clave (keyword arguments) a una función.

# Permite que la función reciba un diccionario con pares clave-valor,
# donde las claves son los nombres de los argumentos y los valores son los datos pasados a la función.


# El doble asterisco (**) indica que el argumento es un diccionario que contiene los argumentos de palabras claves.
# En la definición de la función, se le asigna un nombre a este diccionario.


# Utilizar funcion kwargs para imprimir datos de un diccionario o conjuto	

# def saludar(**kwargs):
#     if "nombre" in kwargs:
#         print(f"Hola, {kwargs['nombre']}!")
#     else:
#         print("Hola, desconocido")
#     if "edad" in kwargs:
#         print(f"Tienes {kwargs['edad']} años.")

# saludar(nombre = "Martin")
# saludar(nombre = "Alonso", edad = 17)
# saludar()

# |-----------|-------------------------------|------------------------------|
# | elemento  |	       que recibe           |	como lo usa la funcion	   |
# |-----------|-------------------------------|------------------------------|
# |*args	    |	varios valores sin nombre   |	como una tupla((a, b, c))  |
# |**kwargs   |	varios valores con nombre   |	como un diccinario ({}     |
# |-----------|-------------------------------|------------------------------|
# Nota sobre *args vs **kwargs

# *args captura argumentos posicionales
# **kwargs caputa argumentos nombrados (clave = valor)

# *args vs **kwargs

# def mostrar(*args, **kwargs):
# 	print("Posicionales: ", args)
# 	print("Nombrados: ", kwargs)

# mostrar(1, 2, 3, nombre ="Yetzibel", edad = 18)


# def mostrar_frutas(*frutas, **detalles):
#     print("=== Lista de frutas ===")
#     for fruta in frutas:
#         print(f"- {fruta}")
#     print("\n=== Detalles adicionales ===")
#     for clave, valor in detalles.items():
#         print(f"{clave}: {valor}")
# mostrar_frutas("Manzana", "plátanos", "Naranja", color_favorito="Rojo", cantidad = 3, estacion = "Verano")



