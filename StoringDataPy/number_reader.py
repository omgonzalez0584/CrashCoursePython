#Leer datos de un archivo json

import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(type(numbers))
print(numbers)
