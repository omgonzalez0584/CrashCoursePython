#Guarda el nombre de un usuario en un archivo

#Ruta del archivo
filename = 'guest.txt'

with open(filename,'a') as file:
    name = input("Introduzca su nombre: ")
    file.write(name + "\n")
