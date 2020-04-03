from country_codes import get_country_code
import json
from pygal.maps.world import COUNTRIES

filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

pop_data2010 = []
for dictionary  in pop_data:
    if dictionary['Year'] == '2010':
        pop_data2010.append(dictionary)


#print(len(pop_data2010))
#print(pop_data2010)

pop_temp = []
for countries in pop_data2010:
    code = get_country_code(countries['Country Name'])
    if code == None:
        print(countries['Country Name'])

print(COUNTRIES)
