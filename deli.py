
#Lista de sandwich ordenados por los clientes
sandwich_orders = ['tuna','pastrani', 'chicken','pastrani','beef','pastrani']

#Sacar Pastrani del las ordenes
print("Deli has run out of pastrani")


while 'pastrani' in sandwich_orders:
    sandwich_orders.remove('pastrani')

finished_sandwiches = []

#Valida que los sandwiches esten listos
while sandwich_orders:
    orders = sandwich_orders.pop()
    finished_sandwiches.append(orders)
    print("I made your "+orders+" sandwich.")

#Imprime los sandwich terminados
print("\nList of sandwich finished:")
for sandwich in finished_sandwiches:
    print(sandwich)






