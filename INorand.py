print("Asignaturas optativas Año 2020")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la ASIGNATURA ESCOGIDA: ")

asignaturas=opcion.lower()

if asignaturas in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):

	print("ASIGNATURA ESCOGIDA: " + asignaturas)

else:
	
	print("La asignatura escogida no esta contemplada")