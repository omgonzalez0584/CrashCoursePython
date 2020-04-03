#Programa almacena tres diccionarios en una lista

#creacion de diccionarios
people_0 = {'firstname':'omar','lastname':'gonzalez','city':'arraijan'}
people_1 = {'firstname':'ambar','lastname':'gonzalez','city':'lagos'}
people_2 = {'firstname':'mia','lastname':'pinzon','city':'villa lucre'}

#creacion de lista
people_list = []

#Agregar elementos a la lista
people_list.append(people_0)
people_list.append(people_1)
people_list.append(people_2)

#print(people)

#Desplegar informacion de la lista
print("\nLista de personas: ")
for people in people_list:
    print("Firstname: "+people['firstname'].title())
    print("Lastname: "+people['lastname'].title())
    print("city: "+people['city'].title())
    print("\n")
