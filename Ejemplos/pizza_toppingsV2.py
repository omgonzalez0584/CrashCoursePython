#Agregar ingredientes de una pizza
# practica 7-4

toppings_list = [] #Lista donde se guardan los toppings

while True:
    topping = input("Enter the topping for your pizza(Quit for exit): ")

    if topping == 'quit':
        break
    else:
        toppings_list.append(topping)
        print("You will add that topping in your pizza!")

print("Topping list")
print(toppings_list)


