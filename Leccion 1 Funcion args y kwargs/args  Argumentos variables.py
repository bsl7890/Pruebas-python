# Esta función suma todos los números que le pases.
# *args convierte todos los números en una tupla (como una lista, pero no se puede modificar).
def sumar_todo(*numeros):  
    total = 0
    for n in numeros:  # 👉 Recorre cada número recibido
        total += n
    return total

print(sumar_todo(1, 2, 3))           # 👉 Suma 1+2+3 = 6
print(sumar_todo(10, 20, 30, 40))    # 👉 Suma 10+20+30+40 = 100
print(sumar_todo())    # 👉 Por defecto da 0

#Otra forma de hacerla

def sumar_todo(*numeros):  
    return sum(numeros)

print(sumar_todo(1, 2, 3))           # 👉 Suma 1+2+3 = 6
print(sumar_todo(10, 20, 30, 40))    # 👉 Suma 10+20+30+40 = 100
print(sumar_todo())    # 👉 Por defecto da 0


# Funciones args y kwargs

# En python, a veces queremos crear funciones que puedan recibir cualquier cantidad de datos,
# sin saber cuántos exactamente.

# Para eso usaremos:

# *args: para recibir muchos valores (sin nombre)

# **kwargs: para recibir muchos valores con nombre

# Funciones args y kwargs

# Cuando una funcion se define como * args, se pueden pasar tantos argumentos posicionales 
# como se desee, y estos se agrupan automáticamente en una tupla dentro de la función

# Para que sirven

# para crear funciones flexibles que acepten cualquier cantidad de valores.
# Por ejemplo, funciones matemáticas o de registro
# Para escribir funciones que operan sobre listas de elementos sin saber de antemano
# cuantos habra

# *args es como una lista de cosas que puedes llevar a una reuinion de innnovacion de proyectos

# ej: def llevar(*cosas):
# 	for cosa in cosas:
# 		print(f"Llevo {cosa}")
#     llevar("Lápiz", "Borrador", "Cartulina", "Celular")
