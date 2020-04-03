# Ejemplo de como codificar un diccionario.

fav_language = {
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python',
        }

print("Sarah's favorite language is "+fav_language['sarah'].title()+".")

#Loopeando a traves Clave-Valor 
for name, language in fav_language.items():
    print(name.title()+"'s favorite language is "+
            language.title()+".")

#Loop through all the keys
for name in fav_language.keys():
    print(name.title())

#Ordenando salida del un diccionario
for name in sorted(fav_language.keys()):
    print(name.title()+ ", thank you for taking the poll.")


#Looping through all values in a Diccionary
print("The following languages have been mentioned: ")
for language in fav_language.values():
    print(language.title())









