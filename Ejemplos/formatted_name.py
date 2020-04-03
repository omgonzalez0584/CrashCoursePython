#funcion retornando valores

def get_formatted_name(firstname,lastname,middle_name=""): #argumento opcional
    if middle_name:
        full_name = firstname+' '+middle_name+' '+lastname
    else:
        full_name = firstname+' '+lastname
    
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

#LLamando a la funcion pasando un argumento opcional
musician = get_formatted_name('john','hook','lee')
print(musician)




