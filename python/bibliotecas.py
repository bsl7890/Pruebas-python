"""" benjamin Santader
trabajo de POO sobre una biblioteca escolar.
4°E"""
import re
# Nombre de la biblioteca
nombre_biblioteca = "Biblioteca Escolar Vate"

# Capacidad máxima de libros que puede contener la biblioteca
capacidad_maxima = 1500

# Cantidad actual de libros disponibles
libro_disponibles = 1223

# Diccionario con la información de un libro destacado
libros_destacado = {
    "titulo": "La Conspiración",     # Título del libro
    "autor": "Dan Brown",            # Autor del libro
    "año": 2001,                     # Año de publicación
    "género": "Novela",              # Género literario
    "disponible": True               # Estado de disponibilidad
}

# Lista de categorías de libros disponibles en la biblioteca
categorias = ["Ficcion", "No ficción", "Ciencia", "Historia", "matematica"]

# Horario de atención de la biblioteca: (hora de apertura, hora de cierre)
horario = (9, 17)  # Abre a las 9:00 y cierra a las 17:00

# Conjunto de RUT de estudiantes que actualmente tienen préstamos activos
estudiantes_con_prestamos = {12345678, 2345678, 34567890}

# Mostrar el nombre de la biblioteca
print(nombre_biblioteca)

# Calcular cuántos libros faltan para llegar a la capacidad máxima
libro_faltantes = capacidad_maxima - libro_disponibles

# Agregar una nueva categoría a la lista de categorías
categorias.append("Programación")

# Imprimir el horario de atención de forma amigable
print(f"La hora de apertura es a las {horario[0]}:00 y el cierre es a las {horario[1]}:00.")

# Agregar un nuevo estudiante con préstamo activo al conjunto
estudiantes_con_prestamos.add(12280919)

# Actualizar el estado del libro destacado a "no disponible"
libros_destacado["disponible"] = False

# Mostrar la información actualizada del libro destacado
print(libros_destacado)

# Función que valida el formato de un RUT chileno
def validar_rut(rut):
    # Elimina los puntos del RUT y lo convierte a mayúscula (por si la 'k' está en minúscula)
    rut = rut.replace(".", "").upper()

    # Patrón que verifica que el RUT tenga:
    # - 7 u 8 dígitos
    # - un guion
    # - un dígito verificador que sea número o la letra 'K'
    patron = r"^\d{7,8}-[\dK]$"
    
    # Retorna True si el RUT cumple con el patrón, si no, retorna None (que equivale a False)
    return re.match(patron, rut)

# Bucle que se repite hasta que el usuario escriba un RUT válido
while True:
    # Solicita al usuario que ingrese su RUT
    nuevo_rut = input("Ingrese su RUT (ej: 22.384.522-3): ")

    # Elimina los espacios en blanco del RUT por si el usuario los escribió
    nuevo_rut = nuevo_rut.replace(" ", "")

    # Verifica si el RUT ingresado tiene el formato correcto
    if validar_rut(nuevo_rut):
        # Si es válido, lo agrega al conjunto de estudiantes con préstamo
        estudiantes_con_prestamos.add(nuevo_rut)

        # Muestra mensaje de éxito
        print(f"Se agregó un nuevo RUT: {nuevo_rut}")
        
        # Sale del bucle
        break
    else:
        # Si el RUT es inválido, muestra un mensaje de error y vuelve a pedirlo
        print("El RUT ingresado no es válido. Asegúrate de escribirlo bien (ej: 22384522-3)")
print(estudiantes_con_prestamos)

