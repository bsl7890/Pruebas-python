"""Benjamín Santander Lopez
Actividad: Análisis de Nombres con Argumentos Variables
Fecha: 09/10/2025
Curso: 4°E
"""

# Definimos la función que acepta un número variable de argumentos posicionales y de palabras clave
def analizar_nombres(*args, **kwargs):
    if not args:
        print("No se han proporcionado nombres para analizar.")
        return
    print("Análisis de Nombres:\n")
    # Iteramos sobre cada nombre recibido en *args
    for nombre in args:
        # Imprimimos el nombre original
        print("|--------------------------------------------------------|")
        print(f"| Nombre original: '{nombre}'")
        # Aplicamos y mostramos el nombre en minúsculas
        print(f"| Minúsculas: '{nombre.lower()}'")
        # Aplicamos y mostramos el nombre en mayúsculas
        print(f"| Mayúsculas: '{nombre.upper()}'")
        # Aplicamos y mostramos el nombre con la primera letra en mayúscula
        print(f"| Primera letra mayúscula: '{nombre.strip().capitalize()}'")
        # Aplicamos y mostramos el nombre con la primera letra de cada palabra en mayúscula
        print(f"| Título: '{nombre.title()}'")
        # Aplicamos y mostramos el nombre con mayúsculas y minúsculas intercambiadas
        print(f"| Swapcase: '{nombre.swapcase()}'")
        # Aplicamos y mostramos el nombre sin espacios al inicio y al final
        print(f"| Sin espacios (strip): '{nombre.strip()}'")
        # Aplicamos y mostramos el nombre sin espacios al inicio
        print(f"| Sin espacios al inicio (lstrip): '{nombre.lstrip()}'")
        # Aplicamos y mostramos el nombre sin espacios al final
        print(f"| Sin espacios al final (rstrip): '{nombre.rstrip()}'")
        print("|--------------------------------------------------------|")
        # Imprimimos una línea en blanco para separar los resultados de cada nombre
        print()
        # Si se proporcionaron datos adicionales en **kwargs, los imprimimos
        if kwargs:
            print("Datos adicionales proporcionados:")
            print("-------------------------------")
            print()
            
            # Imprimimos los datos adicionales recibidos en **kwargs
            for clave, valor in kwargs.items():
                print(f"{clave.capitalize()}: {valor}")
            print()
            input("Presiona Enter para continuar...\n")
    # Imprimimos el nombre y apellidos del autor del programa
    print("Programa realizado por: Benjamín Santander Lopez\n")
# Llamamos a la función con varios nombres y datos adicionales
analizar_nombres("  paulina salgado  ", curso="4°B", año=2025)
analizar_nombres("FRANCISCA santibañez", curso = "4°C", año=2025)
analizar_nombres("lOREna LoPEZ", curso = "4°G" , año=2025)