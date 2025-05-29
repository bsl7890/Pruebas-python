# Esta función saluda a una persona. Si no se entrega un nombre, usa "Benjamín" por defecto.
def saludar(nombre="Benjamín"):  
    print(f"Hola, {nombre}!")

saludar()               # 👉 No se entrega nombre, usa el valor por defecto.
saludar("Ignacio")      # 👉 Se entrega "Ignacio", reemplaza el valor por defecto.
