import random
import string

# 1. Pedir al usuario la longitud
longitud = int(input("¿Cuántos caracteres quieres que tenga tu contraseña? (mínimo 8): "))

# 2. Verificar si es válida
if longitud < 8:
    print("La contraseña debe tener al menos 8 caracteres.")
    exit()

# 3. Crear el conjunto de caracteres
caracteres = string.ascii_letters + string.digits + string.punctuation

# 4. Generar la contraseña
contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

# 5. Mostrarla
print("Tu contraseña segura es:", contraseña)
