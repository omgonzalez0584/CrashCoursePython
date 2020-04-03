#Version de remenber_me refactorizada
#dividiendo en funciones

import json

def get_stored_name():
    """Obtiene el username almacenado en el json file"""
    filename = 'username.json'
    try:
        with open(filename)  as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_user():
    """Guarda el username en el json file"""
    username = input("What is your name?:  ")
    filename = 'username.json'

    with open(filename,'w') as file
        json.dump(username,file)
        print("We'll remenber you when you come back, " + username.title() + "!")


def greet_user():
    """Saludo a usuario, si el username ya esta almacenado en el json"""
    username = get_stored_name()

    if username:
        print("Welcome back, " + username + "!")
    else:
        get_new_user()

#Main del programa
greet_user()


##
