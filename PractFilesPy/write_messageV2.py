#Appending to a file

filename = 'programming.txt'

with open(filename,'a') as file:
    file.write("I also finding meaning in large datasets.\n")
    file.write("I love creating apps that can run  in a browser.\n")
