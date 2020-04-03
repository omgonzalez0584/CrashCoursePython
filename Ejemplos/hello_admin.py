

usernames = ['omar','mia','ambar','berta','admin','arturo']
usernames = [] #para validar cuando la lista esta vacia.


if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello "+username+", would you like to see a status report?")
        else:
            print("Hello "+username+" thank you for logging again")
else:
    print("We need to find some users!")





