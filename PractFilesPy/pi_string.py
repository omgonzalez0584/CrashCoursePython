#Working with file's content

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print("PI: " + pi_string)
print("Cantidad de digitos: " + str(len(pi_string)))
