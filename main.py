import numpy as np

import matplotlib as plt

import user_csv

def get_country_input():
        
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

    resort_data = user_csv.read_csv("resorts", 1)      #gets csv of ski resort data
    
    valid_countries = []

    for i in range(len(resort_data)):                           #iterates through the length of the ski resorts and indexes the locations to a valid region list
        if(resort_data[i][4] not in valid_countries):             #removes duplicate countries from valid regions list
            valid_countries.append(resort_data[i][4])
        valid_countries.sort()                                        #alphabetize list
    
    while True:
        print('To exit the program, type -')
        input_region = input("Input your country here: ").title().strip()     #Ask for input regions
        

        valid_countries.sort()                                        #alphabetize list
        if(input_region == '0'):
            for i in range(len(valid_countries)):                     #print nicely formatted list
                print(f'{i} - {valid_countries[i]}')

        elif(not np.isin(input_region, valid_countries)):             #print error message if input is not valid
            
            if(input_region == '-'):                                  #check for exit condition
                break
            else:
                print("I am sorry, your country is not in our database")
                print("To print a list of countries, enter 0")
        
        else:
            print("valid")                                            #aknowlage valid selection and exit the main function loop
            break
    
    return input_region


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

def print_resorts_in_country(country):
    '''
    input country
    output a list of the ski resort and its respective ID number
    '''
    resort_data = user_csv.read_csv("resorts", 1)      #gets csv of ski resort data

    resort_list = []

    for i in range(len(resort_data)):
        
        resort_ID = [str(resort_data[i][1]), int(resort_data[i][0])]        #structure resorts to have the ID number and the name
        if country == resort_data[i][4]:                                    #If the country is in the list, add the ID and name of the resort to the list
            resort_list.append(resort_ID)
            

        
    resort_list.sort()                                                      #alphabetize the list

    print(f'resorts in {country}')
    print('Resort Number - Resort Name')
    for j in range(len(resort_list)):                                       #print list of restorts
        
        print(f'{j+1} - {resort_list[j][0]}')

    return resort_list

def select_resort(resort_list):

    '''
    input list[[resort name, resort ID],...]
    output list resort ID and name
    '''
    while True:
        user_resort = int(input("input the resort number here: "))

        indexnumber = -1

        if 0 < user_resort <= len(resort_list):
            indexnumber = resort_list[user_resort-1][1]
            print(f'You selected {resort_list[user_resort-1][0]}')
            break
        else:
            print("Invalid Input, please try again")

    return indexnumber



    '''
    Parameters: country in list of possible countries

    Returns: list of ski resorts in country

    Structure:
    Bennet can you write the docstrings for this code?  I dont fully understand it
    thanks pookie <3
    
    '''

    resort_data = user_csv.read_csv("resorts", 1)     #gets csv of ski resort data

    resorts_list = []                                   #empty list to store resorts in the specified region
    
    for row in resort_data:
        mountain_region = row[4]                        #indexing the region column
        
        mountain_name = row[1]                          #indexing the resort name column
        
        mountain_id = row[0]

        if mountain_region == country:                   #checking if the resort's region matches the input region
            resorts_list.append(mountain_name + ',' + str(mountain_id))           #adding the resort name to the list if it matches
            

    print(f"Resorts in {country}:")
    
    
    
    resorts_list.sort()                                        #alphabetize list

    for i in range(len(resorts_list)):                         #print nicely formatted list
        
        resorts_list[i].split(',')
        print(f'{i} - {resorts_list[i]}')


    return resorts_list

def average_price(resort_list, country):
    #turns resort_list into numpy array for easier indexing
    resort_list = np.array(resort_list)
    col = 1
    avg = (resort_list[:, col].astype(float).mean())*1.63  #average price of ski resort day tickets from Euro to CAD -- As type fixes the string issue
    print(f'The average price of a ski resort day ticket in {country} is ${avg:.2f} CAD')
    return avg


def print_stats():

    return
#Main Program

print('Welcome to the Ski resort database!')

while True:
    input_country = get_country_input()

    if(input_country == '-'):       #break out of loop for exit sequence
        break

    resort_opt = print_resorts_in_country(input_country)

    skiresortselection = input("To get the average price of the resorts in this country, type 'avg' otherwise type 'select' to select a resort: ").lower().strip()
    
    if skiresortselection == 'avg':
        average_price(resort_opt, input_country)
    elif skiresortselection == 'difficulty':
        difficulty_stats(resort_opt)
    elif skiresortselection =='select':
        select_resort(resort_opt)


print('Thank you for using our program.')       #ending message
