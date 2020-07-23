class Coche():
	def desplazamiento(self):
		print("Me desplazo utilizando cuatro ruedas")

		
class Moto():
	def desplazamiento(self):
		print("Me desplazo utilizando dos ruedas")

class Camion():
	def desplazamiento(self):
		print("Me desplaz usando seis ruedas")


def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()


miVehiculo=Moto()

desplazamientoVehiculo(miVehiculo)