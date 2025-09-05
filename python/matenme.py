class empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre= nombre
        self.edad = edad
        self.salario = salario
    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * (porcentaje / 100)
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años. y mi salario es: {self.salario}")
class gerente(empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)  
        self.departamento = departamento
    def mostrarinfo(self):
        print(f"Mi departamento es: {self.departamento}")
class Desarrollador(empleado):
    def __init__(self, nombre, edad, salario, lenguaje):
        super().__init__(nombre, edad, salario)  
        self.lenguaje = lenguaje
    def mostrarinfo(self):
        print(f"Mi lenguaje de programacion es: {self.lenguaje}")

gerente1 = gerente("Carlos", 45, 5000000, "Recursos Humanos")
desarrollador1 = Desarrollador("Ana", 30, 3000000, "Python")

gerente1.saludar()
gerente1.mostrarinfo()
desarrollador1.saludar()
desarrollador1.mostrarinfo()

# Aumentar el salario
gerente1.aumentar_salario(10)  
desarrollador1.aumentar_salario(25)  

print("\nDespués del aumento de salario:")
gerente1.saludar()
desarrollador1.saludar()