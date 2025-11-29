import numpy as np

import matplotlib as plt

import user_csv

def get_region_input():
    resort_data = user_csv.read_csv("resorts", 1)      #gets csv of ski resort data
    while True:
        input_region = input("input your country here: ").title().strip()     #Ask for input regions

        valid_regions = []                                                  
        for i in range(len(resort_data)):                           #iterates through the length of the ski resorts and indexes the locations to a valid region list
            if(resort_data[i][4] not in valid_regions):             #removes duplicate countries from valid regions list
                valid_regions.append(resort_data[i][4])

        valid_regions.sort()                                        #alphabetize list
        if(input_region == '0'):
            for i in range(len(valid_regions)):                     #print nicely formatted list
                print(f'{i} - {valid_regions[i]}')
            
        elif(not np.isin(input_region, valid_regions)):
            print("Invalid region. Please enter a valid state or province from the following list:")
            print("To print a list of valid regions enter 0")

        else:
            print("valid")
            return input_region
            break


    return input_region

def resorts_in_region(region):
    resort_data = user_csv.read_csv("resorts", 1)     #gets csv of ski resort data
    resorts_list = []                                   #empty list to store resorts in the specified region
    for row in resort_data:
        mountain_region = row[4]                        #indexing the region column
        mountain_name = row[1]                          #indexing the resort name column
        if mountain_region == region:                   #checking if the resort's region matches the input region
            resorts_list.append(mountain_name)          #adding the resort name to the list if it matches

    print(f"Resorts in {region}:")
    resorts_list.sort()                                        #alphabetize list
    for i in range(len(resorts_list)):                     #print nicely formatted list
        print(f'{i} - {resorts_list[i]}')
    return resorts_list

input_region = get_region_input()
resorts_in_region(input_region)


'''
#ask what ski pass the user has either ikon or epic 1 or 2 or 3 for both?
def get_pass_input():
    input_pass = input("Please enter the ski pass you have (e.g., ikon, epic, both): ").lower().strip()
    valid_passes = ["ikon", "epic", "both"]
    while input_pass not in valid_passes:
        print("Invalid pass. Please enter a valid ski pass from the following list:")
        print(", ".join(valid_passes))
        input_pass = input("Please enter the ski pass you have (e.g., ikon, epic, none): ").lower().strip()
    return input_pass


#print mountains in that region that accept that pass a list of limited and a list of unlimited
def filter_mountains_by_region_and_pass(data, region, ski_pass):
    filtered_mountains = []
    for row in data:
        mountain_region = row[0] 
        mountain_passes = row[2]
        if mountain_region.upper() == region:
            if ski_pass == "BOTH" or ski_pass in mountain:
                filtered_mountains.append(row)
                return filtered_mountains

        else:
            return ["No mountains found in that region that accept that pass"]

'''


#Sorting Options:
    #Max runs
#def max_runs(data):
    

    #Max vertical
    #Max acres


    #longest run takes mile or km input from user and converts if needed to km output and sorts by longest to shortestst

 
    #Average snowfall - Calculate the season average based on all avalible data for that resort
