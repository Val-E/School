num = int(input("Give a integer: "))
nums = list(range(3,num,2))

if num < 1:
    print("Keine Primzahl")

elif num == 2:
    print("Primzahl")

else:
    k = 1
    for i in nums:
        if num % i == 0:
            k = 0       
        else:
            pass
			
if k == 1:
    print(str(num) + " ist eine Primzahl.")
	
else:
    print(str(num) + " ist keine Primzahl")	