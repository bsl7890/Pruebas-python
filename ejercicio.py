# Nombre: Benjamin Santander López
# Curso: 4° Medio
# Fecha: 23 de julio de 2025
# Descripción: Programa que crea una carpeta y un archivo de texto con una historia,
# y elimina la letra A al inicio y las letras R, T, Q, P, Y, 9 al final de cada línea usando lstrip(), rstrip(), for y la librería os.

import os

# Paso 1: Crear carpeta llamada CLASE
ruta_carpeta = "C:/CLASE"

# Verificar si la carpeta fue creada o no
try:
    os.makedirs(ruta_carpeta, exist_ok=False)
    print(f"La carpeta fue creada con éxito en: {ruta_carpeta}")
except PermissionError:
    print(f"No tiene permiso para crear carpetas en {ruta_carpeta}")
except Exception as e:
    print(f"Ocurrió un error: {e}")   

# Paso 2: Crear archivo "cuento.txt"
ruta_archivo = os.path.join(ruta_carpeta, "cuento.txt")

# Paso 3: Escribir la historia
historia = """AEn el futuro brillante vivía la familia Supersónico, con su perro Astro y el robot RobotinaR.
ASúper Sónico volaba a su trabajo en un platillo, mientras Ultra Sónico hacía las compras con solo presionar un botónT.
ALucero Sónico soñaba con ser cantante galáctica, y Cometín Sónico inventaba robots para no hacer la tareaQ.
AUn día, Astro se perdió entre satélites y meteoritosP.
ATodos lo buscaron con su nave turbo y, al encontrarlo, hicieron una fiesta entre estrellasY.
ADesde entonces, los Supersónicos valoraron más estar juntos que cualquier tecnología9."""

# Guardamos el texto en el archivo de texto
with open(ruta_archivo, 'w') as archivo:
    archivo.write(historia)

# Paso 4: Leer las líneas
with open(ruta_archivo, 'r') as archivo:
    lineas = archivo.readlines()

# Aplicar lstrip() para quitar la A al inicio
lineas_sin_A = [linea.lstrip("A") for linea in lineas]

with open(ruta_archivo, 'w') as archivo:
    archivo.writelines(lineas_sin_A)

# Segunda pasada: eliminar letras específicas al final
with open(ruta_archivo, 'r') as archivo:
    lineas = archivo.readlines()

# Quitar salto de línea temporalmente, luego quitar '.', luego las letras, y finalmente añadir salto de línea y punto.
lineas_finales = []
for linea in lineas:
    linea_sin_salto = linea.rstrip('\n')         # Quitar salto de línea para procesar
    linea_sin_punto = linea_sin_salto.rstrip('.') # Quitar punto si está al final
    linea_sin_letras = linea_sin_punto.rstrip("RTQPY9") # Quitar letras indicadas al final
    linea_final = linea_sin_letras + '.' + '\n'  # Añadir punto y salto de línea
    lineas_finales.append(linea_final) # Guardamos las lineas a añadir en una lista

# Guardar las líneas finales en el archivo
with open(ruta_archivo, 'w') as archivo:
    archivo.writelines(lineas_finales)