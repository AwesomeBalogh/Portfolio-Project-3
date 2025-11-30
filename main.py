import numpy as np

import matplotlib as plt

import user_csv

def get_region_input():
    resort_data = user_csv.read_csv("resorts", 1)      #gets csv of ski resort data
    valid_regions = []                                                  
    for i in range(len(resort_data)):                           #iterates through the length of the ski resorts and indexes the locations to a valid region list
        if(resort_data[i][4] not in valid_regions):             #removes duplicate countries from valid regions list
            valid_regions.append(resort_data[i][4])
        valid_regions.sort()                                        #alphabetize list
    
    while True:
        input_region = input("Input your country here: ").title().strip()     #Ask for input regions

        if(input_region == '0'):
            for i in range(len(valid_regions)):                     #print nicely formatted list
                print(f'{i} - {valid_regions[i]}')
            
        elif(not np.isin(input_region, valid_regions)):
            print("Invalid region. Please enter a valid country:")
            print("To print a list of valid regions enter 0")

        else:
            print("valid")
            return input_region

def region_rows_list(region):
    data = user_csv.read_csv("resorts", 1)             #gets csv of ski resort data             
    rows = []
    for i in range(len(data)):
        if data[i][4] == region:
            rows.append(data[i])
    print(rows)    
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
        print(f'{i + 1} - {resorts_list[i]}')
    return resorts_list

def average_price():
    data = user_csv.read_csv("resorts", 1)     #gets csv of ski resort data 
    prices = []
    for i in range(len(data)):
            prices.append(int(data[i][6]))                  #adding valid prices to list

    if len(prices) > 0:
        average = np.average(prices)                   #using numpy to calculate average
        print(f"The average price of lift tickets across all resorts is: €{average:.2f}")


#Main Program

input_region = get_region_input()
resorts_in_region(input_region)





