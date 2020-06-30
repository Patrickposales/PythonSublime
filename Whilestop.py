import math

print("Programa de calculo de raiz cuadrada")
Num=int(input("Introduce un numero por favor: "))

intentos=0

while Num<0:
	print("No se puede hallar la raiz de un numero negativo")

	if intentos==2:
		print("Has consumido todos los intentos. El programa ha finalizado")
		break;

	Num=int(input("Introduce un numero por favor: "))
	if Num<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(Num)
	print ("La raiz cuadradade " + str(Num) + " es " + str(solucion))




