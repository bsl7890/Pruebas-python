"""""Benjamín santander 4° Medio E
"""

# Función para mostrar componentes
def mostrar_componente(*cantidad_componentes):  
    # Imprime un encabezado
    print("Componentes de la computadora:")
    # Recorre e imprime cada componente recibido como argumento
    for componente in cantidad_componentes:
        print(f"- {componente}")

# Función para mostrar nombre y detalles de un componente
def detalles_componente(nombre_componente, **detalles):
    # Muestra el nombre del componente
    print(f"Detalles del componente {nombre_componente}:")
    # Recorre el diccionario de detalles y los muestra
    for clave, valor in detalles.items():
        print(f"{clave}: {valor}")

# Función para ensamblar una computadora con partes y detalles del técnico
def ensamblar_computadora(*partes, **detalles_tecnico):
    # Muestra las partes que se están ensamblando
    print("Ensamblando computadora con las siguientes partes:")
    for parte in partes:
        print(f"- {parte}")
    # Muestra la información del técnico
    print("\nDetalles del técnico:")
    for clave, valor in detalles_tecnico.items():
        print(f"{clave}: {valor}")

# Llamado a la función para mostrar varios componentes
mostrar_componente("Procesador", "Memoria RAM", "Disco Duro", "Tarjeta Gráfica")

# Llamado a la función para mostrar detalles de un componente específico
detalles_componente("Procesador", marca="Intel", velocidad="3.5 GHz", núcleos=4)

# Llamado a la función para ensamblar una computadora y mostrar datos del técnico
ensamblar_computadora(
    "Placa Madre", "Fuente de Poder", "Gabinete",        # Argumentos normales (partes)
    tecnico="Juan Pérez", fecha="2023-10-01", tipo_gabinete="ATX"  # Argumentos nombrados (kwargs)
)
