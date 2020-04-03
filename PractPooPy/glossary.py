#Manejo de un glosario usando un diccionario

from collections import OrderedDict

glossary = OrderedDict()

glossary['POO'] = 'Programacion Orientada a Objetos'
glossary['loop'] = 'Ciclos repetitivos'
glossary['lista'] = 'Guarda un Conjunto de elemetos'
glossary['modulo'] = 'Conjunto de funciones en un archivo'

for word, definition in glossary.items():
    print(word.title() + ": "+definition.title())
