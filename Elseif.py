print("Verificacion de accesso")

edad_usuario=int(input("confirme su edad, por favor: "))

if edad_usuario<18:
	print("prohibido la entrada a menores, favor retitarse del evento")
elif edad_usuario>100:
	print("Edad incorrecta")
else:
	print("puede pasar, disfrute del evento")
print("El programa ha finalizado, muy buen resto del dia")