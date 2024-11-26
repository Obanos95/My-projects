country = {'FR': 'France',   # Countries according to their ISO 3166-1 alpha-2 code
           'DE': 'Germany',
           'ES': 'Spain',
           'GB': 'England'}

def de():
    return country['DE']

def isITACountry():
    if 'IT' in country:
        return True
    else:
        return False
    
def ifWeCallIT():
    return "If we try to call 'IT' code, the program will raise an error because there's no code 'IT' in the list"

def callCountry():
    if 'FR' in country.keys():
        return country['FR']
    else:
        return "UNKNOWN"

def addIT():
    country.update({'IT':'Italy'})
    return country

def changeGB():
    country.update({'GB':'United Kingdom'})
    return country

def showCodes():
    for i in country:
        print(i)

def showCountries():
    for i in country.values():
        print(i)

def showCouples():
    for i in country:
        print(f'({i},{country[i]})')

def countryContent():
    for i in country:
        print(f'{i} -> {country[i]}')


print(de()) # Get the country corresponding to the code 'DE'
print(isITACountry()) # Find out if the code 'IT' is in country
print(ifWeCallIT()) # What happens if we want to retrieve the country associated with 'IT'
print(callCountry()) # Get a country corresponds to a code (for example 'IT' or 'FR') and 'UNKNOWN' if there is no country associated with the code
country = addIT() # Add the country Italy associated with the IT code
print(country)
country = changeGB() # Change the country associated with 'GB' to 'United Kingdom'
print(country)
showCodes() # Show all possible codes
showCountries() # Show all countries
showCouples() # Display all couples (code, country)
countryContent() # Display country content in the form code -> country