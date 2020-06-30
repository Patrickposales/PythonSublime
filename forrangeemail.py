contador=False
miEmail=input("Introduce tu direccion de email: ")

for i in range(len(miEmail)):

	if miEmail[i]=="@":
		contador=True

if contador:
	print("Email correcto")

else:

	print("Email incorrecto")