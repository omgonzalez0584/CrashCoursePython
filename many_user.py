#Anidar diccionarios

#Creacion de diccionario anidado
user = {
    'aeinstein':{
         'first':'albert',
         'last':'einstein',
         'location':'princeton',
         },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        }
    }

#extraer data del diccionario
for username , user_info in user.items(): #items devuelve una lista de tuplas con clave y valor
    print("\nUsername: "+username)
    full_name = user_info['first'] + " "+user_info['last']
    location = user_info['location']

    print("\tFull name: "+full_name.title())
    print("\tLocation: "+location.title())
