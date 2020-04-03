#Practicas de Capitulo 10 de Archivos

filename = 'learning_python.txt'
"""10.1 Learning Python - Aplicando las tres maneras de leer un archivo. """
with open(filename) as file:
    #Lee el archivo entero
    print("\nLee el archivo completo")
    content = file.read()
    print(content)

#Lee el archivo linea por linea
print("Lee el archivo linea por linea: ")
with open(filename)  as file:
    for line in file:
        print(line.rstrip())

#Guarda el Archivo en una lista
print("Guarda el archivo en un lista: ")
with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        print(line.rstrip())


print("\n")
"""10.2 Learning C - Leer un archivo y reemplazar python por C """
print("Reemplazando Python por lenguaje C: ")
with open(filename) as file:
    lines = file.readlines()

mensaje = ''
for line in lines:
    mensaje = line
    print(mensaje.replace('Python','C').strip())
    mensaje = ''

####
