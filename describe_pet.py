#Funciones con Keyword Argument

def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type+".")
    print("My "+ animal_type + "'s name is "+pet_name.title()+".")

#LLamada  la funcion
describe_pet(animal_type = 'hamster', pet_name = 'harry') #<- Uso de Keyword Argument
describe_pet(pet_name = 'harry',animal_type='hamster')


