# Esta función suma todos los números que le pases.
# *args convierte todos los números en una tupla (como una lista, pero no se puede modificar).
def sumar_todo(*numeros):  
    total = 0
    for n in numeros:  # 👉 Recorre cada número recibido
        total += n
    return total

print(sumar_todo(1, 2, 3))           # 👉 Suma 1+2+3 = 6
print(sumar_todo(10, 20, 30, 40))    # 👉 Suma 10+20+30+40 = 100
