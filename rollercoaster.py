#Uso de la funcion input() y int()

height = input("\nHow tall are you , in inches? ")
height = int(height) #Convertir String a numero entero

if height >= 36:
    print("\n You're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
