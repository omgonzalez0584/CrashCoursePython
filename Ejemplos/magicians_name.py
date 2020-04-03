#Pasa como argumento una lista

#Imprime una lista de magos
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

#modifica la lista
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = 'Great '+ magicians[i]
    
    return magicians

#Creacion de lista
magicians = ['merlin','salomon','gandalf']

great_magic = make_great(magicians[:])
show_magicians(magicians) #LLamada a la funcion
show_magicians(great_magic) 




