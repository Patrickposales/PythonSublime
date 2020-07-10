class coche():

	def __init__(self):


		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False

	def arrancar(self,arrancamos):
		self.__enmarcha=arrancamos

		if(self.__enmarcha):

			return "El coche esta en marcha"
		else:

			return "El coche esta parado"


		

	def estado(self):
		print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de",self.__anchoChasis, "Y un largoChasis de",
			self.__largoChasis)


miCoche=coche()


print(miCoche.arrancar(True))

miCoche.estado()

print("----------A continuacion creamos el segundo objeto-------------")

miCoche2=coche()


print (miCoche2.arrancar(False))

miCoche2.__ruedas=2

miCoche2.estado()


