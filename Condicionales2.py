salario_presidente=int(input("Introduzca salario del Presidente: "))
print("Salario presidente: " + str(salario_presidente))	

salario_director=int(input("Introduzca salario del Director: "))
print("Salario director: " + str(salario_director))	

salario_jefe_area=int(input("Introduzca salario del Jefe de Area: "))
print("Salario Jefe Area: " + str(salario_jefe_area))	

salario_administrativo=int(input("Introduzca salario del Administrativo: "))
print("Salario administrativo: " + str(salario_administrativo))		

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("¯\_(ツ)_/¯Las botellas estan bien alimentadas")
else:
	print("ヽ(ಠ_ಠ)ノ Wait thats illegal")