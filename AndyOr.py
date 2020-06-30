print("Programa de becas Año 2020")
distancia_escuela=int(input("Introduce la distancia a la escuela en Km: "))
print(distancia_escuela)

numero_hermano=int(input("Introduce el n° de hermanos enel centro: "))
print(numero_hermano)

salario_familiar=int(input("Introduce salario anual bruto: "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermano>2 or salario_familiar<=20000:
	print("Tiene derecho a becas")
else:
	print("No tiene derecho a becas")