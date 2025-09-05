def procesar(nombre, *actividades, edad=18, **extras):
    print(f"Nombre: {nombre} - Edad: {edad}")
    print("Actividades:")
    for act in actividades:
        print(f" - {act}")
    print("Extras:")
    for clave, valor in extras.items():
        print(f"   {clave}: {valor}")

procesar("Benjamín", "Programar", "Hacer ejercicio", comuna="La Granja", curso="4° Medio")
