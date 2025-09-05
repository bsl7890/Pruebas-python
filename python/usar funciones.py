def es_par(numero):
    if numero % 2 == 0: # Division residual EJ: 8 / 2 = 4 // 4*2 = 8 // 8-8 = 0
        return True
    else:
        return False
    
def cuadrado(x):
    return x * x
def suma_de_cuadrados (a,b):
    return cuadrado(a) + cuadrado(b)

resultado = suma_de_cuadrados(2,3)
print(f"El resultado de la suma de cuadrados es: {resultado}")

#Ejemplo; Uso de funcion sum
numeros = [30, 4 , 2025]
def suma(x):
    return sum(x)
print("El resultado es: ", suma(numeros)) # 2059

#Sumar con un valor inicial

numeros = [30, 4, 2025]
resultado_anterior = sum(numeros, 10)
print(f"EL resultado es la suma de los 3 primeros valores + 10 es: {resultado_anterior}")
#El resultado es la suma de los 3 primeros valores + 10 es: 2069

#Ejemplo: uso de funcion range

valores= range(1, 5)

print("Los valores existente son: ", list(valores))
# Los valores existente son: [0, 1, 2, 3, 4]

valores = range(2, 10, 2)

print("Los valores que incluye en rango son: ", list(valores))
# Los valores que incluye el rango son: [2, 4, 6, 8]

# range(2,10,1) el 2 es con el numero que inicia y el 10 es hasta cuanto va a terminar y el 1 es cuanto anvazara paso a paso es decir 1, 2, 3 , 4 hasta 10 

# Crear un rango descendente

valores_descendente = range(10, 0, -1)

print("Los valores que incluye el rango son:", list(valores_descendente))
#Los valores que incluye el rango son [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]