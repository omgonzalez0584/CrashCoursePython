#Funcion que imprime la ciudad y su pais 

def city_country(city,country):
    flag = city+","+country
    return flag.title()

flag = city_country('santiago','chile')
print(flag)
flag = city_country('Buenos Aires','argentina')
print(flag)
flag = city_country('panama','panama')
print(flag)




