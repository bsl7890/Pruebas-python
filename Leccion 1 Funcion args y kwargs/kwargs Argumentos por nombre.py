# Esta función acepta argumentos con nombre, como nombre="Benjamín", edad=18, etc.
# Los convierte en un diccionario llamado "datos".
def mostrar_info(**datos):  
    # .items() convierte el diccionario en una lista de pares (clave, valor)
    # Ejemplo: {"nombre": "Benjamín"} → ("nombre", "Benjamín")
    for clave, valor in datos.items():  
        print(f"{clave}: {valor}")  # Muestra cada clave con su valor

# Llamamos a la función con 3 datos nombrados
mostrar_info(nombre="Benjamín", edad=18, curso="4° Medio")
# 👉 Imprime:
# nombre: Benjamín
# edad: 18
# curso: 4° Medio
