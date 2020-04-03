#Valida si tu fecha de nacimiento esta en el PI

filename = 'pi_million_digits.txt'

with open(filename) as file:
    lines = file.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Ingrese la fecha de su nacimiento(mmddyy): ")

if birthday in pi_string:
    print("Tu fecha de nacimiento aparece en el primer millon de digitos del PI")
else:
    print("Tu fecha de nacimiento no aparece..")

    
