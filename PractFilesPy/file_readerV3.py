#Making a list of lines from a file

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines() #metodo que guarda lineas en una lista

#print(type(lines))
#print(lines)

for line in lines:
    print(line.rstrip())
