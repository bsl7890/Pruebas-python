empleados = []

def agregar_empleado(nombre, cargo):
    empleado = {
        "nombre": nombre,
        "cargo": cargo
    }
    empleados.append(empleado)
    print(f"Empleado {nombre} agregado con éxito.")
    pass


def listar_empleados():
    if not empleados:
        print("No hay empleados registrados.")
    else:
        print("Lista de empleados:")
        for empleado in empleados:
            print(f"Nombre: {empleado['nombre']}, Cargo: {empleado['cargo']}")
    pass