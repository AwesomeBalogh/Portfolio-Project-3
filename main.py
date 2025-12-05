import numpy as np

import matplotlib.pyplot as plt

import user_csv
#===========================================================Function Definitions===========================================================
def get_country_input():
    ''' Gets user input for country, and displays valid countries if requested. 
    Parameters: none
    Return: input country
    '''

    resort_data = user_csv.read_csv("resorts", 1)      #gets csv of ski resort data
    
    valid_countries = []

    for i in range(len(resort_data)):                           #iterates through the length of the ski resorts and indexes the locations to a valid region list
        if(resort_data[i][4] not in valid_countries):             #removes duplicate countries from valid regions list
            valid_countries.append(resort_data[i][4])
        valid_countries.sort()                                        #alphabetize list
    
    while True:
        input_region = input("Input your country here. (To exit the program, type 'Leave'): ").title().strip()     #Ask for input regions
        valid_countries.sort()                                        #alphabetize list
        if(input_region == '0'):
            for i in range(len(valid_countries)):
                print(f'{i} - {valid_countries[i]}')     
                

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

    print(f'\nHere are the resorts in {country}:\n')

    #for j in range(len(resort_list)):                                       #print list of restorts OLD
    #    print(f'{j+1} - {resort_list[j][0]}')

    for i in range(0, len(resort_list), 3):                     #print 3 resorts per line  JORDAN LMK if you like this, some resorts have very long names though!!    
        print(
            f"{i+1:2d} - {resort_list[i][0]:35s}"
            + (f"{i+2:2d} - {resort_list[i+1][0]:35s}" if i+1 < len(resort_list) else "")
            + (f"{i+3:2d} - {resort_list[i+2][0]:35s}" if i+2 < len(resort_list) else "")
            )
    print()  # Add an extra newline for better readability

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

def average_price(country):
    """
    Compute the average ski resort day ticket price in CAD.

    Converts the price data (column 1) from a list of resorts to floats,
    finds the mean, converts from EUR to CAD, prints a message, and
    returns the average.

    Parameters:
    Country : str
        Country name used in the printed output.
    Returns:
    float
        Average price in CAD.
    """
    resort_data = user_csv.read_csv("resorts", 1)      # gets csv of ski resort data
    resort_stats = user_csv.read_csv("Resort price and features", 0)  # gets csv of ski resort stats
    prices_cad = []
    for i in range(len(resort_data)):
        if resort_data[i][4] == country:
            price_eur = float(resort_stats[i][1])
            prices_cad.append(price_eur*1.63) # Convert EUR to CAD

    avg = np.mean(prices_cad)
    return avg

def max_difficulty(index_number, country):               #fix 
    run_data = user_csv.read_csv('resort runs', 1)

    data = []  # use a Python list first

    for i in range(len(index_number)):
        idx = index_number[i][1] - 1   # convert to 0-based
        data.append(run_data[idx])

    data = np.array(data)  # convert to NumPy at the end

    beg = np.max(data[:, 1])

    beg_idx =index_number[np.argmax(data[:, 1])][0] 

    adv = np.max(data[:, 3])

    adv_idx =index_number[np.argmax(data[:, 3])][0]

    print(f'The best resort for beginners in {country} is {beg_idx}, having {beg} beginner runs.\n')
    print(f'The best resort for advanced runs in {country} is {adv_idx}, having {adv} beginner runs.\n')

    return

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

#===========================================================Visualization Functions===========================================================
def hist_prices(country):
    """
    Show a histogram of day ticket prices (in CAD)
    for all resorts in a given country, without using try/except.
    """
    resort_data = user_csv.read_csv("resorts", 1)
    resort_stats = user_csv.read_csv("Resort price and features", 0)

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
    """
    Show a scatter plot of day ticket prices (in CAD)
    vs number of lifts for all resorts in a given country.
    """
    resort_data = user_csv.read_csv("resorts", 1)
    resort_stats = user_csv.read_csv("Resort price and features", 0)

    prices_cad = []
    num_lifts = []

    for i in range(len(resort_data)):
        if resort_data[i][4] == country:
            price_eur = float(resort_stats[i][1])
            price_cad = price_eur * 1.63
            lifts = int(resort_stats[i][8])
            prices_cad.append(price_cad)
            num_lifts.append(lifts)

    plt.figure()
    plt.scatter(num_lifts, prices_cad)
    plt.title(f'Day Ticket Prices vs Number of Lifts in {country}')
    plt.xlabel('Number of Lifts')
    plt.ylabel('Day Ticket Price (CAD)')
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

while True:
    input_country = get_country_input()

    if(input_country == 'Leave'):       #break out of loop for exit sequence
        break

    resort_opt = print_resorts_in_country(input_country)

    menu_input = input(
    "Choose from the following options:\n"
    "Select     - Select a resort to view its statistics.\n"
    "Average   - Finds the average ticket price of all resorts in this country\n"
    "Histogram  - Displays a histogram of the day ticket price by the number of resorts in the country.\n"
    "Difficulty - resort with maximum difficulty\n"
    "Scatter    - price vs number of lifts scatter plot\n"
    "\nEnter selection: "
    ).lower().strip()


    #Added a bunch of other possible inputs for dummy proofing.

    if menu_input in ('average','avg'):
        avg = average_price(input_country)
        print(f'The average price of a ski resort day ticket in {input_country} is ${avg:.2f} CAD.')

    elif menu_input in ('histogram', 'hist'):
        hist_prices(input_country)

    elif menu_input in ('diff', 'difficulty'):
        max_difficulty(resort_opt, input_country)

    elif menu_input in ('select', 'select resort', 'resort', 'view'):
        index = select_resort(resort_opt)
        print(index)
        print_stats(index)

    elif menu_input  in ('scatter', 'scatter plot', 'plot', 'scat'):
        scatter_price_vs_lifts(input_country)

    else:
        print("Invalid input, please try again.")

print('Thank you for using our program.')       #ending message