lambda argumentos: expresión
# En Python, una función lambda es una función anónima que se define en una sola línea.

#ejemplo de función lambda

# Función normal
def cuadrado(x):
    return x * x

# Lambda
cuadrado_lambda = lambda x: x * x # Función lambda equivalente
# Ambas funciones hacen lo mismo, pero la función lambda es más corta y se usa comúnmente para funciones simples o de una sola línea.

print(cuadrado(4))         # 16
print(cuadrado_lambda(4))  # 16
