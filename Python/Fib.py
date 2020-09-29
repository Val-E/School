def Fib():

	a = 1
	
	while a <= 2:
		a = int(input("Bitte geben Sie an welche Fibonacchizahl ausgegeben werden soll (Die Zahl muss größer sein als zwei.): "))
	list = [0,3]
	a = a - 1
	while a != 1:
		a = a - 1
		plist = [list[-1] + list[-2]]
		list = list + plist
		
	print(list)
	
	
Fib()