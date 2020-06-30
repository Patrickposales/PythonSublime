print("Calificacion digital de alumnons")

nota_alumno=input("introduce la nota del alumno: ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion


print(evaluacion(int(nota_alumno)))