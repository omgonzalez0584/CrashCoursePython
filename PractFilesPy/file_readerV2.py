#Reading file line by line

filename = 'pi_digits.txt' #almacenando ruta del archivo

#Abriendo archivo y creando objeto
with open(filename) as file_object:
    for line in file_object:
        print(line)
