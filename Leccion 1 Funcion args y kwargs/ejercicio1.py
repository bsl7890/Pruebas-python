def resumen_personal (nombre, edad, **otros_datos):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")

    for clave,valor in otros_datos.items():
        print(f"{clave}: {valor}")

resumen_personal("benjamin", 18, colegio = "Vate", curso = "4° Medio E")
