# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:47:46 2023

@author: ethan.drover
"""

# =============================================================================
#          Creating Dictionairies

# Syntax: example_dict = {key 1:value 1,
#                key 2:value 2}
#
# Dictionairies are mutable
# =============================================================================

countries = {'CA':'Canada',
             'US':'United States',
             'MX':'Mexico'}

movie = {'name': 'Robocop',
         'year': 1987,
         'price':9.99}

# Retrieving values for a particular key

country = countries['CA']

# Methods, get() function

country = countries.get('US')
country = countries.get('IN', 'Unknown')

# Updating values for an existing key

countries['CA'] = 'Cameroon'

# Adding to a dictionairy
countries['IN'] = 'India'
# Properties
country_code = 'MX'

if country_code in countries:
    country = countries[country_code]   
    print(country)
else:
    print(f"No country for this code {country_code}")
    

# Delete a key value pair

del countries['CA']
del country, country_code

country = countries.pop('US')
movie.clear()

# Accessing keys

goose = countries.keys()
print(f'Country codes: {goose}')
        
    
for code2 in countries.keys():
    print(f'{code2}\t\t{countries[code2]}')

# Accessing values

countries.values()

for country in countries.values():
    print(country)
    
# Accessing both the keys and values

countries.items()

for country_code, country in countries.items():
    print(f'{country_code}\t\t{country}')

# Converting keys,values,items to a list

list(countries.keys())        
list(countries.values())       
list(countries.items())            

# Converting from a list
countries_list = [['GB','Britain'],
              ['NL','Netherlands'],
              ['DE','Germany']]

dict(countries_list)
countries_list2 = [['GB','Britain','EU'],
              ['NL','Netherlands','America'],
              ['DE','Germany','EU']]

dict(countries_list2)
