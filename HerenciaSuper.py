class Persona():

	def __init__(self,nombre,edad,Lugar_residencia):
		self.nombre=nombre
		self.edad=edad
		self.lugar_residencia=Lugar_residencia

	def descripcion(self):
		print("Nombre: ", self.nombre,"|", " Edad: ", self.edad, "|", " Residdencia: ", self.lugar_residencia)

class Empleados(Persona):

	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residdencia_empleado):

		super().__init__(nombre_empleado, edad_empleado ,residdencia_empleado)

		self.salario=salario

		self.antiguedad=antiguedad

	def descripcion(self):

		super().descripcion()
		print(" Salario: ", "|", self.salario, "|", " Antiguedad: ", self.antiguedad)


Muriel=Persona("Muriel", 35, "Alemania")

Muriel.descripcion()

print(isinstance(Muriel, Empleados))