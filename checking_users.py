
current_users = ['omar','ambar','mia','berta','mimi','mia']

new_users = ['arturo','ambar', 'mia','bodoque','astrid']

for new_user in new_users:
    if new_user in current_users:
        print("The username has already been used.")
    else:
        print("The username is availble.")

        
