import json

#Load the username , if it has been stored previously.
#Otherwise, prompt for the username and store it
filename = 'username.json'
try:
    with open(filename) as file_obj:
        username = json.load(file_obj)
except FileNotFoundError:
    username = input("what is your name?  ")
    with open(filename,'w') as file_obj:
        json.dump(username,file_obj)
        print("We'll remenber you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
