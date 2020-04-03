#Definiendo la clase User

class User():
    """ Cuerpo de la clase User"""

    def __init__(self,first_name,last_name,age,location):
        """Constructor de la clase"""
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age
        self.location = location

    def describe_user(self):
        """ Metodo que despliega la informacion del usuario"""
        print("Informacion del usuario: ")
        print("First Name: "+self.first_name)
        print("Last Name: "+self.last_name)
        print("Edad: "+str(self.age))
        print("Ubicacion: "+self.location)

    def greet_user(self):
        """Envia un saludo al usuario"""
        print("\nHola "+self.first_name)



#Instanciando objeto
user = User('Omar','Gonzalez',35,'Arraijan')
user_2 = User('Bodoque','Bodoque',2,'Pedasi')
#LLamando a metodos
user.describe_user()
user.greet_user()

user_2.describe_user()
user_2.greet_user()










