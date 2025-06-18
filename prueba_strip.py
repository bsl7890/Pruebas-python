
print("\n*******************************************\n")

# .strip() es un método de cadena en Python que elimina los espacios en blanco al principio y al final de una cadena.

# prueba de strip

def prueba_strip():
    cadena = "   Hola, mundo!   "
    cadena_strip = cadena.strip()
    print(f"Cadena original: '{cadena}'")
    print(f"Cadena después de strip: '{cadena_strip}'")

prueba_strip()

print("\n*******************************************\n")

#.strip() funciona tambien para las listas, eliminando espacios en blanco al principio y al final de cada elemento de la lista.


def prueba_strip_lista():
    lista = ["   Hola", "mundo!   ", "  Python  "]
    lista_strip = [elemento.strip() for elemento in lista]
    print("Lista original:", lista)
    print("Lista después de strip:", lista_strip)

prueba_strip_lista()

print("\n*******************************************\n")

#lstrip() elimina espacios en blanco solo al principio y rstrip() solo al final.

def prueba_lstrip_rstrip():
    cadena = "   Hola, mundo!   "
    cadena_lstrip = cadena.lstrip()
    cadena_rstrip = cadena.rstrip()
    print(f"Cadena original: '{cadena}'")
    print(f"Cadena después de lstrip: '{cadena_lstrip}'")
    print(f"Cadena después de rstrip: '{cadena_rstrip}'")

prueba_lstrip_rstrip()

print("\n*******************************************\n")
# para colocar la letra mayuscula al principio de una cadena se puede usar el método capitalize()
def prueba_capitalize():
    cadena = "hola, mundo!"
    cadena_capitalize = cadena.capitalize()
    print(f"Cadena original: '{cadena}'")
    print(f"Cadena después de capitalize: '{cadena_capitalize}'")

prueba_capitalize()

print("\n*******************************************\n")
# para colocar la primera letra de cada palabra en mayuscula se puede usar el método title()
def prueba_title():
    cadena = "hola, mundo! bienvenido a python."
    cadena_title = cadena.title()
    print(f"Cadena original: '{cadena}'")
    print(f"Cadena después de title: '{cadena_title}'")
prueba_title()
