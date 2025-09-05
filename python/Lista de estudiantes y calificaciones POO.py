# Benjamín Santander
# Trabajo de POO sobre una biblioteca escolar.
# 4°E

# Lista de estudiantes con sus nombres y notas
estudiantes = [
    {"nombre": "Martin", "nota": 50},   # Estudiante 1
    {"nombre": "Carlos", "nota": 62},   # Estudiante 2
    {"nombre": "Juan", "nota": 70},     # Estudiante 3
    {"nombre": "Roberto", "nota": 38},  # Estudiante 4
    {"nombre": "David", "nota": 40},    # Estudiante 5
]
# Mostrar todos los estudiantes de la lista con sus nombres y notas
for linea in estudiantes:
    print(f"Nombre: {linea['nombre']}, Nota: {linea['nota']}")
# Agrega un nuevo estudiante con su respectiva nota
nombre = "benjamin"  # Nombre del nuevo estudiante
nota = 23  # Nota del nuevo estudiante
estudiantes.append({"nombre": nombre , "nota": nota})  # Agregamos el estudiante a la lista

# Imprime un indicador que se agregó un nuevo estudiante
print(f"\nSe agregó un nuevo estudiante: {nombre} con nota {nota}\n")

# Mostrar nuevamente la lista de estudiantes después de agregar el nuevo estudiante
for linea in estudiantes:
    print(f"Nombre: {linea['nombre']}, Nota: {linea['nota']}")


# Inicialización de las variables necesarias para calcular el promedio y encontrar la mejor nota
suma_notas = 0           # Variable para sumar las notas
mejor_estudiante = ""    # Variable para almacenar el nombre del estudiante con la mejor nota
mejor_nota = 0           # Variable para almacenar la mejor nota

# Iteración sobre la lista de estudiantes para calcular la suma de notas y encontrar la mejor nota
for estudiante in estudiantes:
    nombre = estudiante["nombre"]  # Obtenemos el nombre del estudiante
    nota = estudiante["nota"]     # Obtenemos la nota del estudiante
    
    suma_notas += nota  # Sumamos la nota del estudiante a la variable suma_notas
    
    # Comprobamos si la nota del estudiante es la mejor hasta ahora
    if nota > mejor_nota:
        mejor_nota = nota  # Actualizamos la mejor nota
        mejor_estudiante = nombre  # Actualizamos el estudiante con la mejor nota

# Calculamos el promedio de las notas dividiendo la suma total de las notas por el número de estudiantes
promedio = suma_notas / len(estudiantes)

# Imprimimos el promedio con 2 decimales
print(f"\nEl promedio de notas es: {promedio:.1f}")

# Imprimimos el estudiante con la mejor nota
print(f"\nEl estudiante con la mejor nota es {mejor_estudiante} con {mejor_nota}")

# Imprimimos los estudiantes cuya nota está por encima del promedio
print("\nEstudiantes por encima del promedio:")
for estudiante in estudiantes:
    if estudiante["nota"] > promedio:  # Si la nota del estudiante es mayor al promedio
        print(f"- {estudiante['nombre']} ({estudiante['nota']})")  # Imprimimos el nombre y la nota

# Mostrar la nota más baja y contar estudiantes por encima y por debajo del promedio
nota_baja = min(estudiante["nota"] for estudiante in estudiantes)  # Nota más baja
print(f"\nLa nota más baja es: {nota_baja}")

# Contamos cuántos estudiantes tienen una nota por encima del promedio
por_encima_promedio = sum(1 for estudiante in estudiantes if estudiante["nota"] > promedio)
# Contamos cuántos estudiantes tienen una nota por debajo del promedio
por_debajo_promedio = sum(1 for estudiante in estudiantes if estudiante["nota"] < promedio)

# Imprimimos la cantidad de estudiantes por encima y por debajo del promedio
print(f"\nCantidad de estudiantes por encima del promedio: {por_encima_promedio}")
print(f"Cantidad de estudiantes por debajo del promedio: {por_debajo_promedio}")

# Ingresar datos manualmente de estudiantes
while True:
    # Solicitamos al usuario si desea agregar un nuevo estudiante
    respuesta = input("\n¿Deseas agregar un nuevo estudiante? (si/no): ").lower()
    if respuesta == "si":
        # Si la respuesta es sí, pedimos el nombre del nuevo estudiante
        nombre = input("Ingrese el nombre del estudiante: ")
        
        # Buscamos si el estudiante ya existe en la lista
        for estudiante in estudiantes:  
            if estudiante["nombre"].lower() == nombre.lower():  # Comparamos en minúsculas para evitar problemas de mayúsculas/minúsculas
                # Si ya existe, le damos la opción de cambiar la nota
                nueva_nota = int(input(f"\nIngrese la nueva nota para {nombre}: "))
                estudiante["nota"] = nueva_nota  # Actualizamos la nota
                print(f"\nSe actualizó la nota de {nombre} a {nueva_nota}")
                break  # Salimos del ciclo si ya se actualizó la nota
        else:
            # Si el estudiante no existe, lo agregamos con la nueva nota
            nueva_nota = int(input(f"Ingrese la nota para {nombre}: "))
            estudiantes.append({"nombre": nombre, "nota": nueva_nota})  # Añadimos el nuevo estudiante a la lista
            print(f"\nSe agregó un nuevo estudiante: {nombre} con nota {nueva_nota}")
    elif respuesta == "no":
        break  # Si la respuesta es no, terminamos el ciclo
    else:
        print("Por favor, ingrese 'si' o 'no'.")  # Si la respuesta no es válida, mostramos un mensaje

# Mostrar todos los estudiantes después de posibles cambios
for linea in estudiantes:
    print(f"Nombre: {linea['nombre']}, Nota: {linea['nota']}")        

# Limpiamos la lista de estudiantes antes de intentar cargarla desde un archivo
estudiantes = []

# Intentamos abrir el archivo 'estudiante.txt' para leer los datos
try:
    with open("C:\\Users\\Alumno\\Documents\\Benjamin Santander\\Pruebas-python\\estudiante.txt", "r") as archivo:  # Abrimos el archivo en modo lectura 
        print("\nContenido del archivo 'estudiante.txt':\n")
        for linea in archivo:  # Leemos cada línea del archivo
            print(linea.strip())  # Muestra la línea del archivo sin espacios extra al inicio y final
            partes = linea.strip().split(",")  # Dividimos la línea en nombre y nota
            if len(partes) == 2:  # Verificamos que se obtengan dos partes (nombre y nota)
                nombre, nota = partes  # Asignamos los valores a las variables
                estudiantes.append({"nombre": nombre, "nota": int(nota)})  # Agregamos al estudiante a la lista
            else:
                print(f"Línea inválida en el archivo: '{linea.strip()}' (se ignoró)")  # Si la línea no tiene el formato correcto, se ignora
except FileNotFoundError:  # Si no se encuentra el archivo
    print("\nEl archivo 'estudiante.txt' no fue encontrado. Se usará una lista predeterminada.")  # Imprime un mensaje de error
    # Lista predeterminada de estudiantes si no se encuentra el archivo
    estudiantes = [
        {"nombre": "Martin", "nota": 50},
        {"nombre": "Carlos", "nota": 62},
        {"nombre": "Juan", "nota": 70},
        {"nombre": "Roberto", "nota": 38},
        {"nombre": "David", "nota": 40},
    ]
