n = 1
notas = []
while True:
    try:
        while n <= 4:
            nota = int(input("Ingrese la nota del alumno: "))
            nombre = input("Ingrese el nombre del alumno: ")
            notas.append((nombre, nota))
            n += 1
        break
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")
        continue


