#Creacion de la clase Restaurant

class Restaurant():
    
    def __init__(self,name,type_cousine):
        self.name = name
        self.type_cousine = type_cousine

    def describe_restaurant(self):
        print(self.name)
        print(self.type_cousine)

    def open_restaurant(self):
        print("Buenos dias, el restaurante esta abierto!")


#Instanciando un objeto de la clase Restaurant
restaurant = Restaurant('McDonald','Fast Food')

#llamando a los metodos
restaurant.describe_restaurant()
restaurant.open_restaurant()

#instanciando 3 objetos
restaurant_1 = Restaurant('Tomillo','Grill')
restaurant_1.describe_restaurant()









