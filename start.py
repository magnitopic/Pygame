month=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
userInput=input("Introduce un mes en número: ")
j=True
while j:
	try:
		if int(userInput)-1<0:
			raise ValueError('ERROR')
		print(f"El mes que has elegido es {month[(int(userInput)-1)]}")
	except:
		print("El valor introducido es incorrecto. Vuelve a intentarlo.")
		userInput=input("Dime un mes en número: ")
	else:
		j=False
