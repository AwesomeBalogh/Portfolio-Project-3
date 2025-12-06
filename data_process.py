import numpy as np

import user_csv

def print_stats(indexnumber):
    '''
    Print ski resort statistics given resort index number
    Param: index number
    Returns: None
    '''
    resort_data = user_csv.read_csv("resorts", 1)      # gets csv of ski resort data
    resort_stats = user_csv.read_csv("Resort price and features", 1)  # gets csv of ski resort stats

    #numpy array of data FYI

    resort_row = None
    stats_row = None
    
    # Find the row in resorts with matching ID
    for row in resort_data:
        resort_id = int(float(row[0]))      #This solves our float int problem to handle '1', '1.0, 1.0
        if resort_id == indexnumber:
            resort_row = row
            break

    # Find the row in stats with matching ID
    for row in resort_stats:
        resort_id = int(float(row[0]))
        if resort_id == indexnumber:
            stats_row = row
            break

    if resort_row is None or stats_row is None:     #This should never run, just in case.
        print("No resort or stats found for that ID.")
        return
    
    resort_name = resort_row[1]
    country = resort_row[4]
    season_length = resort_row[6]

    vertical_drop = int(stats_row[2]) - int(stats_row[3])
    num_lifts = int(stats_row[8])
    price = float(stats_row[1])

    print(f'Statistics for {resort_name} in {country}:')
    print(f'Price of Day Ticket: ${price*1.63:0.2f} CAD')
    print(f'Season Length: {season_length}')
    print(f'Vertical Drop: {vertical_drop:0.2f} Meters')
    print(f'Number of Lifts: {num_lifts}') 
        
    return

def save_resort_list(user_index, country):
    '''
    Saves list of resorts in a country as a CSV file

    Param: user_index: list of resorts in a selected country
                country: User selected country
    
    Return: None
    '''
    filen = input('Enter your File name here: ').strip().title()
    user_csv.write_csv(f'{filen}-{country}', np.array(user_index), 'x')
    return
