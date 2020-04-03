#Validar si un numero es par o impar

number = input("Enter a number, and I'll tell you if its even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number "+str(number)+" is even")
else:
    print("\nThe number "+str(number)+ " is odd.")
