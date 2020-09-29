import turtle, time
 
 
wait = int(input("How long do you want see your polygon (t in s): "))
n = int(input("How many sites your polygon should have: "))
angle = 360/n
s = int(input("How long a site of your polygon should be: "))
 
 
for i in range(n):
    turtle.forward(s)
    turtle.left(angle)
 
 
time.sleep(wait)
