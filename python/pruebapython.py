import os

# Ruta de la carpeta
NuevaCarpeta = input("Ingresa el nombre de la carpeta: ")
ubicacion_carpeta = os.path.join("C:\\Users\\Alumno\\Desktop", NuevaCarpeta)  # Usamos doble barra invertida

# Ruta completa del archivo que se va a crear dentro
ruta_archivo = os.path.join(ubicacion_carpeta, 'archivo_ejemplo.txt')

try:
    os.makedirs(ubicacion_carpeta, exist_ok=False)  # Cambié exist_ok a True para no generar error si ya existe
    print(f"La carpeta fue creada con exito en :\t{ubicacion_carpeta}")
except PermissionError:
    print(f"No tiene permiso para crear carpetas en\t{ubicacion_carpeta}")
except Exception as e:
    print(f"Ocurrio un error:\t{e}")

# Crear un archivo dentro de la carpeta
try:
    with open(ruta_archivo, 'w') as archivo:
        archivo.write("Hola Benjamín!\nEste es un archivo de ejemplo creado con Python.")
    print(f"Archivo creado exitosamente:\t{ruta_archivo}")
except Exception as e:
    print(f"No se pudo crear el archivo:\t{e}")

# Mostrar contenido de la carpeta
if os.path.exists(ubicacion_carpeta):
    contenido = os.listdir(ubicacion_carpeta)
    print("Contenido de la carpeta:")
    if contenido:
        for item in contenido:
            print(f"\t- {item}")
    else:
        print("\t(La carpeta está vacía)")

# Leer el archivo con la ruta correcta
try:
    with open(ruta_archivo, 'r') as archivo:  # Usamos la ruta correcta del archivo
        texto = archivo.read()
        print(f"\nContenido del archivo:\n{texto}")
except Exception as e:
    print(f"No se pudo leer el archivo:\t{e}")
    
try:
    with open(ruta_archivo, "r") as archivo:
        contenidotexto = archivo.read()
        numero = int(contenidotexto)
        print(f"\nEl número leído del archivo es: {numero}")
except FileNotFoundError:
    print("El archivo no se encontró.")
except ValueError:
    print("El contenido del archivo no es un número válido.")
finally:
    print("La operación ha finalizado.")

