# Portfolio Project 3
# Project done by Jordan Kisiler(UCID: 3028396) & Bennett Balogh(UCID:30297254)

import numpy as np

import matplotlib.pyplot as plt

import user_csv

import calculations as calcs

import data_process as datap
#===========================================================Function Definitions===========================================================
def get_country_input():
    ''' 
    Gets user input for country, and displays valid countries if requested. 
    
    Param: None

    Return: validated user input country
    '''

    resort_data = user_csv.read_csv("resorts", 1)      #gets csv of ski resort data
    
    valid_countries = []

    for i in range(len(resort_data)):                           #iterates through the length of the ski resorts and indexes the locations to a valid region list
        if(resort_data[i][4] not in valid_countries):             #removes duplicate countries from valid regions list
            valid_countries.append(resort_data[i][4])
        valid_countries.sort()                                        #alphabetize list
    
    while True:
        input_region = input("Input your country here. (To get a list of avalible countries, type '0'. To exit the program, type 'Leave'): ").title().strip()     #Ask for input regions
        valid_countries.sort()                                        #alphabetize list
        if(input_region == '0'):

            for i in range(0, len(valid_countries), 3):                     #print 3 resorts per line  JORDAN LMK if you like this, some resorts have very long names though!!    
                print(
                f"{i+1:2d} - {valid_countries[i]:35s}"
                + (f"{i+2:2d} - {valid_countries[i+1]:35s}" if i+1 < len(valid_countries) else "")
                + (f"{i+3:2d} - {valid_countries[i+2]:35s}" if i+2 < len(valid_countries) else "")
                )

        elif(input_region == 'Leave'):
            break

        elif(not np.isin(input_region, valid_countries)):             #print error message if input is not valid  
            if(input_region == '-'):                                  #check for exit condition
                break
            else:
                print("I am sorry, your country is not in our database")
                print("To print a list of countries, enter 0")
        
        else:
            break
    
    return input_region

def print_resorts_in_country(country):
    '''
    Print a list of possible resorts in Canada

    Param: user selected country

    Return: list of the ski resort and its respective ID number
    '''
    resort_data = user_csv.read_csv("resorts", 1)      #gets csv of ski resort data

    resort_list = []

    for i in range(len(resort_data)):    
        resort_ID = [str(resort_data[i][1]), int(float(resort_data[i][0]))]
        if country == resort_data[i][4]:                                    #If the country is in the list, add the ID and name of the resort to the list
            resort_list.append(resort_ID)
            
    resort_list.sort()                                                      #alphabetize the list

    print(f'\nHere are the resorts in {country}:\n')

    #for j in range(len(resort_list)):                                       #print list of restorts OLD
    #    print(f'{j+1} - {resort_list[j][0]}')

    for i in range(0, len(resort_list), 3):                     #print 3 resorts per line    
        print(
            f"{i+1:2d} - {resort_list[i][0]:35s}"
            + (f"{i+2:2d} - {resort_list[i+1][0]:35s}" if i+1 < len(resort_list) else "")
            + (f"{i+3:2d} - {resort_list[i+2][0]:35s}" if i+2 < len(resort_list) else "")
            )
    print()  # Add an extra newline for better readability

    #user_csv.write_csv(f'Resorts in {country}',resort_list,'x')     #write CSV for resorts in country and their ID number
    
    return resort_list

def select_resort(resort_list):
    '''
    Validates and returns a selected resort index number.
    
    Param: resort_list : list of [resort_name, resort_ID]
    
    Return: indexnumber : int(resort id)
    '''
    while True:
        user_resort = input("Input the resort number here: ").strip()

        if not user_resort.isdigit():
            print("Please enter a valid number.")
            continue

        user_resort = int(user_resort)

        if 1 <= user_resort <= len(resort_list):
            indexnumber = int(resort_list[user_resort - 1][1])
            print()
            print(f'You selected {resort_list[user_resort - 1][0]}')
            return indexnumber
        else:
            print("Invalid input, please try again.")


#===========================================================Visualization Functions===========================================================
def hist_prices(country):
    '''
    Show a histogram of day ticket prices (in CAD)
    for all resorts in a given country

    Param: user country 

    Return: None
    '''
    resort_data = user_csv.read_csv("resorts", 1)
    resort_stats = user_csv.read_csv("Resort price and features", 1)

    prices_cad = []

    for i in range(len(resort_data)):
        if resort_data[i][4] == country:
            price_eur = float(resort_stats[i][1])
            price_cad = price_eur * 1.63
            prices_cad.append(price_cad)  

    plt.figure()
    plt.hist(prices_cad, bins=10, edgecolor='black')
    plt.title(f'Day Ticket Prices in {country}')
    plt.xlabel('Day ticket price (CAD)')
    plt.ylabel('Number of Resorts')
    plt.show()
    return


def scatter_price_vs_lifts(country):
    '''
    Shows a scatter plot of day ticket prices (in CAD)
    vs number of lifts for all resorts in a given country.
    User can choose a second countrry to overlay
    on the same plot. 

    Parameters: Country
    
    Return: None
    '''
    resort_data = user_csv.read_csv("resorts", 1)
    resort_stats = user_csv.read_csv("Resort price and features", 1)

    valid_countries = []            #Valid countrys code copied from above
    for i in range(len(resort_data)):
        c = str(resort_data[i][4]).strip().title()
        if c not in valid_countries:
            valid_countries.append(c)
    valid_countries.sort()

    prices_cad_1 = []       #Fist country data function
    num_lifts_1 = []

    for i in range(len(resort_data)):
        if str(resort_data[i][4]).strip().title() == country:
            price_eur = float(resort_stats[i][1])
            price_cad = price_eur * 1.63
            lifts = int(resort_stats[i][8])
            prices_cad_1.append(price_cad)
            num_lifts_1.append(lifts)

    if len(num_lifts_1) == 0:           #Should never run just in case
        print(f"No resort data found for {country}.")
        return

    paired1 = []                        #Sort by list
    for i in range(len(num_lifts_1)):
        paired1.append([num_lifts_1[i], prices_cad_1[i]])
    paired1.sort()

    num_lifts_sorted_1 = []
    prices_sorted_1 = []
    for j in paired1:
        num_lifts_sorted_1.append(j[0])
        prices_sorted_1.append(j[1])

    compare_choice = input("Would you like to overlay another country for comparison? (yes/no): ").lower().strip()

    country2 = None
    prices_sorted_2 = []
    num_lifts_sorted_2 = []

    if compare_choice in ("yes", "y"):      #Second country logic
        while True:
            country2_input = input(f"Enter the SECOND country to compare with {country} (or type 'Leave' to cancel): ").title().strip()

            if country2_input == "Leave":
                country2 = None
                break

            if country2_input not in valid_countries:
                print("That country is not in the database. Try again or type 'Leave'.")
            else:
                country2 = country2_input
                break

        if country2 is not None:            #If country is chosen,  get its data
            prices_cad_2 = []
            num_lifts_2 = []

            for i in range(len(resort_data)):
                if str(resort_data[i][4]).strip().title() == country2:
                    price_eur = float(resort_stats[i][1])
                    price_cad = price_eur * 1.63
                    lifts = int(resort_stats[i][8])
                    prices_cad_2.append(price_cad)
                    num_lifts_2.append(lifts)

            if len(num_lifts_2) == 0:           #If no data is found
                print(f"No resort data found for {country2}. Showing only {country}.")
                country2 = None
            else:
                paired2 = []
                for i in range(len(num_lifts_2)):
                    paired2.append([num_lifts_2[i], prices_cad_2[i]])
                paired2.sort()

                for i in paired2:
                    num_lifts_sorted_2.append(i[0])
                    prices_sorted_2.append(i[1])

    plt.figure()
    plt.scatter(num_lifts_sorted_1, prices_sorted_1, alpha=0.7, label=country)      #First Country Plot

    if country2 is not None:                                #Optional second country plot
        plt.scatter(num_lifts_sorted_2, prices_sorted_2, alpha=0.7, label=country2)
        plt.title(f"Day Ticket Prices vs Number of Lifts\n{country} vs {country2}")
    else:
        plt.title(f"Day Ticket Prices vs Number of Lifts in {country}")

    plt.xlabel("Number of Lifts")
    plt.ylabel("Day Ticket Price (CAD)")
    plt.legend()
    plt.show()
    return

#===========================================================Main Program===========================================================
#Prints welcome message and ski resort ASCII art
print('''\t\t      _
                     /#\\
                    /###\\     /\\
                   /  ###\\   /##\\  /\\
                  /      #\\ /####\\/##\\
                 /  /      /   # /  ##\\             _       /\\
               // //  /\\  /    _/  /  #\\ _         /#\\    _/##\\    /\\
              // /   /  \\     /   /    #\\ \\      _/###\\_ /   ##\\__/ _\\
             /  \\   / .. \\   / /   _   { \\ \\   _/       / //    /    \\
     /\\     /    /\\  ...  \\_/   / / \\   } \\ | /  /\\  \\ /  _    /  /    \\ /\\
  _ /  \\  /// / .\\  ..%:.  /... /\\ . \\ {:  \\   /. \\     / \\  /   ___   /  \\
 /.\\ .\\.\\// \\/... \\.::::..... _/..\\ ..\\:|:. .  / .. \\  /.. \\    /...\\ /  \\ \\
/...\\.../..:.\\. ..:::::::..:..... . ...\\{:... / %... \\/..%. \\  /./:..\\__   \\
 .:..\\:..:::....:::;;;;;;::::::::.:::::.\\}.....::%.:. \\ .:::. \\/.%:::.:..\\
::::...:::;;:::::;;;;;;;;;;;;;;:::::;;::{:::::::;;;:..  .:;:... ::;;::::..
;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;];;;;;;;;;;::::::;;;;:.::;;;;;;;;:..\n''')

print('Welcome to the Ski resort database! This code will allow you to explore ski resorts around the world!')   #welcome message

print('Please note: This data was last updated in 2022, so todays data may differ slightly.')

while True:
    input_country = get_country_input()

    if(input_country == 'Leave'):       #break out of loop for exit sequence
        break

    resort_opt = print_resorts_in_country(input_country)        #[[Resort name, resort ID],[Name,ID]...]
    while len(input_country) > 0:
        menu_input = input(
        "Choose from the following options:\n"
        "Select     - Select a resort to view its statistics.\n"
        "Average    - Finds the average ticket price of all resorts in this country.\n"
        "Histogram  - Displays a histogram of the day ticket price by the number of resorts in the country.\n"
        "Difficulty - Display the best resorts for diffrent skill levels.\n"
        "Scatter    - Price vs number of lifts with the option to overlay two plots.\n" \
        "Save       - Save a list of the ski resorts in a country.\n"
        "To return to Country selection, enter 'Leave'.\n"
        "\nEnter selection: "
        ).lower().strip()

        #Added a bunch of other possible inputs for dummy proofing.
        numbers_stuff = []
        for i in range(1000):
            numbers_stuff.append(i)

        if menu_input in ('average','avg'):
            avg = calcs.average_price(input_country)
            print(f'\nThe average price of a ski resort day ticket in {input_country} is ${avg:.2f} CAD.')

        elif menu_input in ('save'):
            datap.save_resort_list(resort_opt,input_country)

        elif menu_input in (str(numbers_stuff)):
            print("Looks like you want to select a resort.")
            index = select_resort(resort_opt)
            datap.print_stats(index)

        elif menu_input in ('histogram', 'hist'):
            hist_prices(input_country)

        elif menu_input in ('diff', 'difficulty'):
            max_vals = calcs.print_max_difficulty(resort_opt)

            print(f'\nThe best resort for beginners skiers in {input_country} is {max_vals[3]}, having {int(max_vals[0])} beginner runs.\n')
            print(f'The best resort for intermediate skiers in {input_country} is {max_vals[4]}, having {int(max_vals[1])} intermediate runs.\n')
            print(f'The best resort for advanced skiers in {input_country} is {max_vals[5]}, having {int(max_vals[2])} advanced runs.\n')

        elif menu_input in ('select', 'select resort', 'resort', 'view'):
            index = select_resort(resort_opt)
            datap.print_stats(index)

        elif menu_input  in ('scatter', 'scatter plot', 'plot', 'scat'):
            scatter_price_vs_lifts(input_country)
            
        elif menu_input == 'leave':
            break

        else:
            print("Invalid input, please try again.")

        print('\n================================================================================================================================\n')

print('Thank you for using our program.')       #ending message