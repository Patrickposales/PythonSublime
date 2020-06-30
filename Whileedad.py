Edad=int(input("Introduce tu edad: "))

while Edad<5 or Edad>100:
	print("Has introducido una edad incorrecta. Favor intente de nuevo")
	Edad=int(input("Introduce tu edad: "))
print("Gracias por colaborar. Puede pasar")
print("Edad del aspirante " + str(Edad))