email=False

for i in "Juan@pildorasinformaticas.es":
	
	if(i=="@"):
		email=True

if email:
	print("Email es correcto")
else:
	print("El email no es correcto")



