import empleados

def calcular_sueldo(base, horas_extra):
    return base + (horas_extra * 5000)

empleados.agregar_empleado("Juan", "Supervisor")
empleados.agregar_empleado("Lucía", "Programadora")

empleados.listar_empleados()

# Calcular sueldo
print("Sueldo de Juan:", calcular_sueldo(500000, 5))
