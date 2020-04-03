from pygal.maps.world import COUNTRIES
#from pygal.i18n import COUNTRIES <--Este ya no se usa

def get_country_code(country_name):
    """Return the pygal 2-digits country code for the given country."""

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    #if the country wasn't found , the return None
    return None
