#Definiendo una clase

class Dog():
    """ Simple attempt to model a dog """

    def __init__(self,name,age):
        """ Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title()+ " is now sitting")

    def roll_over(self):
        """ Simulate rolling over in response to a command"""
        print(self.name.title()+ " rolled over!")

#instanciar objetos
my_dog = Dog('Willie',6)

#Accesando a los atributos
print(my_dog.name)
print(my_dog.age)

#Accesando a los metodos de la clase Dog
my_dog.sit()
my_dog.roll_over()


#Creando multiples instancias o objetos
your_dog = Dog('lucy',3)

your_dog.sit()
your_dog.roll_over()










