def evaluacion(nota):
	valoracion="aprobado"
	if nota<50:
		valoracion="suspenso"
	return valoracion


print(evaluacion(100))