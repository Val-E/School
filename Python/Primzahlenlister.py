import math

def isprime(number):
    if number > 1:
        if number == 2:
            return True

        if number % 2 == 0:
            return False

        for i in range(3, int(math.sqrt(number) + 1), 2):
            if number % i == 0:
                return False
        return True
    return False

def choseprimes(number=2):
    while True:
        if isprime(number):
            yield number
        number += 1


prime_generator = choseprimes()


for i in range(int(input("Bitte geben Sie an, bis zur welchen Primzahl aufgelistet werden soll: "))):
    print(prime_generator.send(None))