def collatz(a):
	while a != 1:
		print(a)
		if a%2 == 0:
			a = a / 2
		else:
			a = a*3 +1
		
			
			
a = int(input("Bitte geben Sie eine Ganzzahl ein: "))
collatz(a)