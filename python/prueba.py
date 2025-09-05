# Aplicar los siguientes temas vistos en clases:  listas, tuplas, conjuntos, try, if, else, for, while, además comentar cada línea de código.

# Actividad 1: 
# Registro de Alumnos y Números de Lista Únicos
# Temas: listas, conjuntos, try, if, else

# Descripción:
# Crea un programa que permita registrar el nombre de los alumnos y su número de lista (único). Si un número de lista ya fue usado, debe mostrar un mensaje de error.

# Requisitos:

# Utiliza una lista de tuplas para almacenar (nombre, número).
# Verifica con un conjunto que los números no se repitan.
# Usa try para manejar exepciones los números deben ser enteros.
# Permite seguir ingresando hasta que se escriba “salir”.

# Actividad 2: 
# Verificador de Votación en Club Escolar Temas: tuplas, listas, if, for, try

# Descripción:
# Determina quiénes pueden votar en una elección del club (mayores de 14 años).

# Requisitos:

# Usa una lista de tuplas con formato: (nombre, edad).
# Verifica con if si pueden votar.
# Usa try para validar que la edad ingresada sea numérica.
# Muestra una lista con los que pueden votar.

# Actividad 3:
# Clasificador de Palabras Únicas y Repetidas
# Temas: listas, conjuntos, for, if, else

# Descripción:
# Clasifica una lista de palabras en dos conjuntos: únicas y repetidas.

# Requisitos:

# Usa una lista para ingresar palabras.
# Usa un conjunto para verificar duplicados.
# Clasifica y muestra resultados con for y if.

# Actividad 4: 
# Juego de Adivina el Número con Historial
# Temas: while, try, listas, if, else

# Descripción:
# Crea un juego donde el usuario intenta adivinar un número del 1 al 20. Guarda los intentos y muestra un resumen al final.

# Requisitos:

# Usa try para validar que el usuario escriba números.
# Usa una lista para guardar los intentos.
# Usa un bucle while para repetir hasta que acierte.
# Usa if-else para dar pistas (mayor o menor).

# Actividad 5:
# Organizador de Clubes Estudiantiles
# Temas: listas, conjuntos, tuplas, for, if

# Descripción:
# Organiza estudiantes por clubes y elimina duplicados entre clubes.

# Requisitos:

# Cada club es una lista de tuplas con (nombre, edad).
# Muestra qué alumnos están en más de un club (usa conjuntos).
# Usa for y if para comparar.

# Suba a classroom cada una de las actividades por separadas, comprimidas en un archivo rar.



#**************************************************************#
#* Ejercicio 1: Registro de Alumnos y Números de Lista Únicos *#
#**************************************************************#

def registro_alumnos():
    """
    Función para registrar alumnos con número de lista único.
    """
    alumnos = []  # Lista para almacenar tuplas (nombre, número)
    numeros_lista = set()  # Conjunto para verificar números únicos
    while True:
        nombre = input("Ingrese el nombre del alumno (o escriba 'salir' para terminar): ")
        if nombre.lower() == "salir":
            break
        try:
            numero = int(input("Ingrese el número de lista: "))
            if numero in numeros_lista:
                print("Error: El número de lista ya fue registrado. Intente con otro número.")
            else:
                numeros_lista.add(numero)
                alumnos.append((nombre, numero))
                print("Alumno registrado correctamente.")
        except ValueError:
            print("Error: Debe ingresar un número entero para el número de lista.")

    print("\nLista de alumnos registrados:")
    for alumno in alumnos:
        print(f"Nombre: {alumno[0]}, Número de lista: {alumno[1]}")

registro_alumnos()

#**************************************************************#
#* Ejercicio 2: Verificador de Votación en Club Escolar       *#
#**************************************************************#


def verificador_votacion():
    """
    Función para verificar qué alumnos pueden votar (mayores de 14 años).
    """
    alumnos_edad = []  # Lista para almacenar tuplas (nombre, edad)
    pueden_votar = []  # Lista para los que pueden votar
    while True:
        nombre = input("Ingrese el nombre del alumno (o escriba 'salir' para terminar): ")
        if nombre.lower() == "salir":
            break
        try:
            edad = int(input("Ingrese la edad del alumno: "))
            alumnos_edad.append((nombre, edad))
        except ValueError:
            print("Error: Debe ingresar un número entero para la edad.")


    for alumno in alumnos_edad:
        if alumno[1] >= 15:
            pueden_votar.append(alumno[0])

    print("\nAlumnos que pueden votar (mayores de 14 años):")
    for nombre in pueden_votar:
        print(nombre)

verificador_votacion()

#**************************************************************#
#* Ejercicio 3: Clasificador de Palabras Únicas y Repetidas   *#
#**************************************************************#

def clasificador_palabras():
    """
    Función para clasificar palabras en únicas y repetidas.
    """
    palabras = []           # Lista para almacenar las palabras ingresadas
    unicas = set()          # Conjunto para palabras únicas
    repetidas = set()       # Conjunto para palabras repetidas
    # Ingreso de palabras por el usuario
    while True:
        palabra = input("Ingrese una palabra (o escriba 'salir' para terminar): ")
        if palabra.lower() == "salir":
            break
        palabras.append(palabra)

    # Clasificación de palabras
    for palabra in palabras:
        if palabra in unicas:
            repetidas.add(palabra)  # Si ya está en únicas, es repetida
        else:
            unicas.add(palabra)     # Si no está, la agregamos a únicas

    # Eliminamos las repetidas del conjunto de únicas
    unicas = unicas - repetidas

    # Mostramos los resultados
    print("\nPalabras únicas:")
    for palabra in unicas:
        print(palabra)

    print("\nPalabras repetidas:")
    for palabra in repetidas:
        print(palabra)

clasificador_palabras()

#**************************************************************#
#* Ejercicio 4: Juego de Adivina el Número con Historial      *#
#**************************************************************#

import random  # Importamos la librería random para generar el número aleatorio

def juego_adivina_numero():
    """
    Función para jugar a adivinar un número del 1 al 20, guardando el historial de intentos.
    """
    numero_secreto = random.randint(1, 20)  # Genera un número aleatorio entre 1 y 20
    intentos = []  # Lista para guardar los intentos del usuario

    print("¡Adivina el número entre 1 y 20!\n")

    while True:
        try:
            intento = int(input("Ingresa tu intento: "))  # Pedimos un número al usuario
            intentos.append(intento)  # Guardamos el intento en la lista

            if intento < numero_secreto:
                print("El número es mayor.")
            elif intento > numero_secreto:
                print("El número es menor.")
            else:
                print("¡Felicidades! Adivinaste el número.")
                break  # Sale del ciclo si adivina
        except ValueError:
            print("Error: Debes ingresar un número entero.")

    # Mostramos el historial de intentos
    print("\nHistorial de intentos:")
    for i, valor in enumerate(intentos, 1):
        print(f"Intento {i}: {valor}")

juego_adivina_numero()

#**************************************************************#
#* Ejercicio 5: Organizador de Clubes Estudiantiles           *#
#**************************************************************#

def organizador_clubes():
    """
    Organiza estudiantes por clubes, muestra cuáles están en más de un club.
    Distingue estudiantes por nombre y edad.
    """
    clubes = {}  # Diccionario para almacenar los clubes y sus miembros
    while True:
        # Solicita el nombre del club
        nombre_club = input("Ingrese el nombre del club (o escriba 'salir' para terminar): ")
        if nombre_club.lower() == "salir":
            break
        miembros = set()  # Usamos un conjunto para evitar duplicados en el mismo club
        print(f"Ingrese los miembros para el club '{nombre_club}' (nombre,edad). Escriba 'fin' para terminar miembros.")
        while True:
            # Solicita los miembros del club
            entrada = input("Miembro (nombre,edad): ")
            if entrada.lower() == "fin":
                break
            try:
                # Separa el nombre y la edad
                nombre, edad = entrada.split(",")
                miembro = (nombre.strip(), int(edad.strip()))  # Crea una tupla (nombre, edad)
                miembros.add(miembro)  # Agrega el miembro al conjunto
            except:
                print("Formato incorrecto. Use: nombre,edad")
        clubes[nombre_club] = miembros  # Asigna los miembros al club en el diccionario

    # Contar en cuántos clubes está cada estudiante (por nombre y edad)
    alumnos_en_clubes = {}

    for miembros in clubes.values():
        for alumno in miembros:
            # Si el alumno ya está en el diccionario, suma 1 al contador
            if alumno in alumnos_en_clubes:
                alumnos_en_clubes[alumno] += 1
            else:
                alumnos_en_clubes[alumno] = 1  # Si no, lo agrega con valor 1

    # Mostrar alumnos que están en más de un club
    print("\nAlumnos que están en más de un club:")
    hay_repetidos = False
    for (nombre, edad), cantidad in alumnos_en_clubes.items():
        if cantidad > 1:
            print(f"{nombre} (edad {edad}) está en {cantidad} clubes")
            hay_repetidos = True
    if not hay_repetidos:
        print("No hay alumnos en más de un club.")
    
    # Mostrar todos los clubes con sus integrantes correspondiente
    print("\nListado de clubes e integrantes:")
    for nombre_club, miembros in clubes.items():
        print(f"\nClub: {nombre_club}")
        if miembros:
            for nombre, edad in miembros:
                print(f" - {nombre} (edad {edad})")
        else:
            print("  (Sin integrantes)")
            
organizador_clubes()



