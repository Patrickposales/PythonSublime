def generaPares(limite):

	num=1

	miLista=[]

	while  num<limite:
		
		yield num*2

		num=num+1

	
devuelvePares=generaPares(10)


for i in devuelvePares:
	print(i)