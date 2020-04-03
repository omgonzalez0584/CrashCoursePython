#Leer un archivos con try-except

def leer_archivos(filename):

    """Lee un archivo e imprime su contenido"""
    try:
        with open(filename) as file_obj:
                content = file_obj.read()
    except FileNotFoundError:
            print("Lo siento, el archivo no se encuentra!")
    else:
        print(content.rstrip())

#Programa principal
archivos = ['cats.txt','dogs.txt','rabbits.txt'] #lista de archivos
i = 1
for archivo in archivos:
    print("Archivo " + str(i) + ":")
    leer_archivos(archivo)
    i += 1
