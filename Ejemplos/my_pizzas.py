#Practica 4-11 realizar copia de una lista

my_pizzas = ['peperoni','meat','jam']
your_pizzas = my_pizzas[:]

my_pizzas.append('pineapple')
your_pizzas.append('sausage')

print("\nMy favorite pizza are: ")
for i in my_pizzas:
    print(i)

print("\nMy friend's favorite pizza are: ")
for i in your_pizzas:
    print(i)




