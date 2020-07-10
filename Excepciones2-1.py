def divide():
	try:

		op1=(float(input("Introduce el primer numero: ")))

		op2=(float(input("Introduce el primer numero: ")))

		print("La division es:" + str(op1/op2))

	except ValueError:

		print("Calculo finalizado")

	except ZeroDivisionError:

		print("No se puede dividir entre 0!")

	print("Calculo finalizado")



divide()