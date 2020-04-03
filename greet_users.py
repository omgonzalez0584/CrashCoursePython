#Funcion que pasa una lista como argumento

def greet_users(names):
    for name in names:
        msg = "Hello, "+name.title()+"!"
        print(msg)

username = ['hannah','ty','margot']
greet_users(username)


