#3-4

guest_list = ['Omar','Ambar','Mia']
print("Buenos dias "+guest_list[0]+" te invito a cenar")
print("Buenos dias "+guest_list[1]+" te invito a cenar")
print("Buenos dias "+guest_list[2]+" te invito a cenar")

#3-5
print(guest_list[0]+" no puede ir a la cena")
guest_list[0] = 'berta'
print("Buenos dias "+guest_list[0].title()+" te invito a cenar!")


#3-6
print("Buenos dias he encontrado una mesa mas grande para la cena!!")
guest_list.insert(0,'Omar')
guest_list.insert(2,'Milton')
guest_list.append('Astrid')
print(guest_list)

print("Buenos dias "+guest_list[0]+" te invito a cenar")
print("Buenos dias "+guest_list[1]+" te invito a cenar")
print("Buenos dias "+guest_list[2]+" te invito a cenar")
print("Buenos dias "+guest_list[3]+" te invito a cenar")
print("Buenos dias "+guest_list[4]+" te invito a cenar")
print("Buenos dias "+guest_list[5]+" te invito a cenar")

#3-7
print("Disculpen solo tengo mesa para dos invitados.....")
flag = guest_list.pop()
print("Lo siento pero.."+flag+" no estas invitado")
flag = guest_list.pop()
print("Lo siento pero.."+flag+" no estas invitado")
print("Lista de invitados: ",guest_list)








