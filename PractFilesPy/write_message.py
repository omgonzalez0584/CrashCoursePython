#Programa sencillo que escribe en un Archivo
filename = 'programming.txt'

with open(filename,'w') as file:
    #Escribiendo multiples lineas
    file.write("I love programming.\n") #\n Es para separar por lineas
    file.write("I love creating new games \n")
