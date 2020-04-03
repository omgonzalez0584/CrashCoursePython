#Registra visitas del usuario en un archivo

filename = 'guest_book.txt'

with open(filename,'a') as file:
    while True:
        name = input("Introduzca su nombre(* para salir): ")
        if name == '*':
            break
        else:
            print("Bienvenido, " + name.title())
            file.write("Nos visita " + name + "\n")
