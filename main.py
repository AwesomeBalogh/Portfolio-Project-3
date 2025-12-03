import numpy as np

import matplotlib.pyplot as plt

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
            return indexnumber
        else:
            print("Invalid Input, please try again")

def average_price(resort_list, country):
    """
    Compute the average ski resort day ticket price in CAD.

    Converts the price data (column 1) from a list of resorts to floats,
    finds the mean, converts from EUR to CAD, prints a message, and
    returns the average.

    Parameters:
    resort_list : list
        List of resort records where column 1 is the price in EUR.
    country : str
        Country name used in the printed output.

    Returns:
    float
        Average price in CAD.
    """
    
    resort_list = np.array(resort_list)                     #convert to numpy array for easier indexing
    col = 1
    avg = (resort_list[:, col].astype(float).mean())*1.63  #average price of ski resort day tickets from Euro to CAD -- As type fixes the string issue
    print(f'The average price of a ski resort day ticket in {country} is ${avg:.2f} CAD')
    return avg

def print_stats(indexnumber):
    '''Print ski resort statistics given resort index number
    Parameters: Index  (internal)
    Returns: None
    '''

    resort_data = user_csv.read_csv("resorts", 1)      # gets csv of ski resort data
    resort_stats = user_csv.read_csv("Resort price and features", 0)  # gets csv of ski resort stats
    
    resort_row = None
    stats_row = None

    for j, row in enumerate(resort_data):                     #They be happy I used enumerate here!!
        if int(row[0]) == indexnumber:
            resort_row = row
            stats_row = resort_stats[j]
            break

    if resort_row is None:                                  # This should never run, just in case
        print(f"No resort found.")
        return select_resort()

    resort_name = resort_row[1]
    country = resort_row[4]
    season_length = resort_row[6]

    vertical_drop = float(stats_row[2]) - float(stats_row[3])
    num_lifts = int(stats_row[8])
    price = float(stats_row[1])

    print(f'Statistics for {resort_name} in {country}:')
    print(f'Price of Day Ticket: ${price*1.63:0.2f} CAD')
    print(f'Season Length: {season_length}')
    print(f'Vertical Drop: {vertical_drop:0.2f} meters')
    print(f'Number of Lifts: {num_lifts}') 
        
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
        print('brokwn')
        #difficulty_stats(resort_opt)
    elif skiresortselection =='select':
        index = select_resort(resort_opt)
        print_stats(index)


print('Thank you for using our program.')       #ending message


#price per resort in a country scatterplot
#bar chart of top 5 countries with most resorts