#Devuelve un diccionario llamado album

def make_album(artist,title_name,track=''): #Paramentro alternativo
    album = {}
    if track:
        album['name'] = artist
        album['title_name'] = title_name
        album['track_number'] = track
    else:
        album['name'] = artist
        album['title'] = title_name
        
    return album

#Ciclo While para ingresar valores
while True:
    artist = input("Introduzca el nombre del Artista(quit para salir): ")
    title_name = input("Introduzca el nombre del Album(quit para salir: )")

    if artist == 'quit' or  title_name == 'quit':
        break
    else:
        album = make_album(artist,title_name)
        print(album)








