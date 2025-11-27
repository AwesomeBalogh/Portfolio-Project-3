import numpy as np

import matplotlib as plt

import user_csv

def get_region_input():
    ski_resort_list_data = user_csv.read_csv("Ski Resort List Data", 1)     #get nested list of [["region", "ski resorts", "Pass", Limited or Unlimited]]
    
    while True:
        input_region = input("Please enter a the state or province you want to ski: (e.g., utah, alberta, colorado): ").lower().strip()     #Ask for input regions
        valid_regions = []                                                  #Creates empty list
        for i in range(len(ski_resort_list_data)):                          #iterates through the length of the ski resorts and indexes the locations to a valid region list
            valid_regions.append(ski_resort_list_data[i])

        if(not np.isin(input_region, valid_regions)):
            print("Invalid region. Please enter a valid state or province from the following list:")
            print("To print a list of valid regions enter 0")

        elif(input_region == '0'):
            print(valid_regions)

    return input_region


get_region_input()


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
