import numpy as np

import matplotlib as plt

import user_csv

def get_country_input():
    resort_data = user_csv.read_csv("resorts", 1)      #gets csv of ski resort data
    
    valid_countries = []

    for i in range(len(resort_data)):                           #iterates through the length of the ski resorts and indexes the locations to a valid region list
        if(resort_data[i][4] not in valid_countries):             #removes duplicate countries from valid regions list
            valid_countries.append(resort_data[i][4])
        valid_countries.sort()                                        #alphabetize list
    
    while True:
        input_region = input("input your country here: ").title().strip()     #Ask for input regions

        valid_countries.sort()                                        #alphabetize list
        if(input_region == '0'):
            for i in range(len(valid_countries)):                     #print nicely formatted list
                print(f'{i} - {valid_countries[i]}')

        elif(not np.isin(input_region, valid_countries)):             #print error message if input is not valid
            print("Invalid region. Please enter a valid country:")
            print("To print a list of valid regions enter 0")

        else:
            print("valid")                                            #aknowlage valid selection and exit the main function loop
            break
            
    '''
    Parameters: none

    Return: input country

    Structure:
    Read resorts.csv
        Make a list of all of the valid countries, filtering out duplicate countries
        Sort countries by alphabetical order
    
    if(input region == '0'): 
        Print a list of valid countries and repropmpt for user input

    elif(input region not in valid countries list):
        Print error and option to print valid country list
        reprompt for user intput

    else:
        break the loop in funtion
    
    
    '''

    return input_region


def region_rows_list(country):                          #what does this do?
    data = user_csv.read_csv("resorts", 1)             #gets csv of ski resort data             
    
    rows = []
    
    for i in range(len(data)):
        if data[i][4] == country:
            rows.append(data[i])
    print(rows)
    '''
    Parameters: country
    read CSV file for resorts
    ???

    '''
    return rows
    


def resorts_in_region(country):
    resort_data = user_csv.read_csv("resorts", 1)     #gets csv of ski resort data
    
    resorts_list = []                                   #empty list to store resorts in the specified region
    
    for row in resort_data:
        mountain_region = row[4]                        #indexing the region column
        
        mountain_name = row[1]                          #indexing the resort name column
        
        if mountain_region == country:                   #checking if the resort's region matches the input region
            resorts_list.append(mountain_name)          #adding the resort name to the list if it matches

    print(f"Resorts in {country}:")
    
    resorts_list.sort()                                        #alphabetize list
    for i in range(len(resorts_list)):                     #print nicely formatted list
        print(f'{i} - {resorts_list[i]}')

    '''
    Parameters: country in list of possible countries

    Returns: list of ski resorts in country

    Structure:
    Bennet can you write the docstrings for this code?  I dont fully understand it
    thanks pookie <3
    
    '''
    return resorts_list

#def average_price(): uncomment when we figure out wtf we are doing with our CSVs

#Main Program
#average_price()                        Uncomment when we know what is happening with the CSV files

input_country = get_country_input()
#region_rows_list(input_country)        Uncomment for testing
resorts_in_region(input_country)
