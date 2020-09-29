import scipy.special
print(",--------------------------===---.")
print("| 	                             |")
print("| ,----------------------------.  |")
print("| |                             | |")
print("| |  Welcome to the             | |")
print("| |                             | |")
print("| |    Bernouilli-Calculator    | |")
print("| |                             | |")
print("| |                             | |")
print("| |                             | |")
print("| |     by Valentin Svet        | |")
print("| |                             | |")
print("| |                             | |")
print("| |                             | |")
print("| |                             | |")
print("| |                             | |")
print("| | P(X=k)=(nCk)*p^k*(1-p)^n-k  | |")
print("| |                             | |")
print("| |.............................| |")
print("| |  _  :          '      :  _  | |")
print("| | |_| :                 : |_| | |")
print("| |  _  :_               _:  _  | |")
print("| | |_| :.)        .    (.: |_| | |")
print("| '-----....._________.....-----' |")
print("|     _    _     O     _    _     |")
print("|    |_|  |_|    |    |_|  |_|    |")
print("'------......____O____......------'")
n = float(input('\n set length n = '))
p = float(input('set probability p = '))
a = []
k = 0
z = 0
q = 0
f = input('Set k by [r]ange or [m]anuelly? [r/m]')

if f == 'm':
	print("Write 'stop' after you added all k's!")
	while(True):
		z += 1
		k = input('set k'+ str(z) + " = ")
		int(z)
		if k == 'stop' or k == '':
			break
		a.append(int(k))
elif f == 'r':
	a = range(int(input('first k = ')),int(input('last k =')) + 1,int(input('steps = ')))
sum = 0
for i in a:
	q = float(scipy.special.binom(n, float(i)))*(p**i)*((1-p)**(n-i))
	sum += q 
	print("P(X = " + str(i) + ")=" + str(q))
	float(q)

print('\n' + 'Sum = ' + str(sum))
