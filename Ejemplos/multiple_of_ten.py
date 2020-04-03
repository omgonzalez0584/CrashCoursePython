#Validar si un numero es multiplo de 10

number = input("Introduzca un numero para validar si un numero es multiplo de 10: ")
number =  int(number)

if number % 10 == 0:
    print(str(number)+" es multiplo de 10")
else:
    print(str(number)+" no es multiplo de 10")
