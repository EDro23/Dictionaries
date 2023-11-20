# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:47:32 2023

@author: ethan.drover
"""
countries = {'CA':'Canada',
             'US':'United States',
             'MX':'Mexico'}

def menu_title():
    print("COMMAND MENU")

def menu_list():
    print("view - View country name\nadd - Add a country")
    print("del - Delete a country\nexit - Exit program")

# Viewing

def view_country():
    goose = countries.keys()
    print(f'Country codes: {goose}')
    
   
    
    
# Adding

def adding_country():
    country_code = input("Enter country code: ")
    name = input("Enter country name: ")
    countries[f'{country_code}'] = f'{name}'
    print(f"{name} was added.")



# Delete
def deleting_country():
    delete = input("Enter country code: ")
    del countries.keys()[f'{delete}']

def main():
    menu_title()
    menu_list()
    while True:
        command = input("Command: ")
    
        if command == 'view':
            view_country()
        elif command == 'add':
            adding_country()
        elif command == 'del':
            deleting_country()
        elif command == 'exit':
            print("Bye!")
            break
    
if __name__ == '__main__':
    main()
        
        
    
    
