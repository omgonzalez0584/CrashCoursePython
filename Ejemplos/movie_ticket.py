#Programa valida el precio de tu boleto 

while True:
    age = input("Ingrese su edad para saber para saber el costo de ticket(quit para salir): ")
    if age == 'quit':
        break
    elif int(age) <= 3:
        print("Su boleto es gratis.")
    elif int(age) > 3 and  int(age) <= 12:
        print("Su boleto cuesta 10$.")
    else:
        print("Su boleto cuesta 15$.")



