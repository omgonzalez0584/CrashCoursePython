#Gross Domestic Product for Country
import json
from country_codes  import get_country_code
from pygal.maps.world import World
from pygal.style import RotateStyle


def extract_code(gross_data):
    """Devuelve un diccionario con los codigos de pais como key
       y el groos como value """
    cc_grossTemp = {}
    for index_dic in gross_data:
        if index_dic['Year'] == 2016:
            code = get_country_code(index_dic['Country Name'])
            if code:
                cc_grossTemp[code] = float(index_dic['Value'])

    return cc_grossTemp

#PROGRAMA PRINCIPAL
filename = 'gdp_json.json'
with open(filename) as f:
    gross_data = json.load(f)

#Extrayendo codigos y valores
cc_gross = extract_code(gross_data)

#Generando el mapa con los datos extraidos
wm_style = RotateStyle('#B3FF11')
wm = World(style=wm_style)
wm.title = "Gross Domestic Product 2016, by Country"
wm.add('Gross', cc_gross)
wm.render_to_file('gdp.svg')
