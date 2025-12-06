import numpy as np

import user_csv

def average_price(country):
    '''
    Compute the average ski resort day ticket price in CAD.

    Converts the price data (column 1) from a list of resorts to floats,
    finds the mean, converts from EUR to CAD, prints a message, and
    returns the average.

    Param: country

    Returns: float(Average price in CAD.)
    '''
    resort_data = user_csv.read_csv("resorts", 1)      # gets csv of ski resort data
    resort_stats = user_csv.read_csv("Resort price and features", 1)  # gets csv of ski resort stats
    prices_cad = []
    for i in range(len(resort_data)):
        if resort_data[i][4] == country:
            price_eur = float(resort_stats[i][1])
            prices_cad.append(price_eur*1.63) # Convert EUR to CAD

    avg = np.mean(prices_cad)
    return avg

def print_max_difficulty(index_number):
    '''
    Find the resorts that are best suited to diffrent level of skiers based on the number of runs in that skill level
    
    Param: index number

    Returns: max number beginner resort runs, beginner resort row index,
             max number intermediate resort runs, intermediate resort row index,
             max number advanced resort runs, advanced resort row index,
    '''

    run_data = user_csv.read_csv('resort runs', 1)

    data = []  # use a Python list first

    for i in range(len(index_number)):
        idx = int(index_number[i][1] - 1)   # convert to 0-based
        data.append(run_data[idx])

    data = np.array(data)  # convert to NumPy at the end
    
    beg = np.max(data[:, 1])

    beg_idx =index_number[np.argmax(data[:, 1])][0] 

    med = np.max(data[:, 2])

    med_idx =index_number[np.argmax(data[:, 2])][0] 

    adv = np.max(data[:, 3])

    adv_idx =index_number[np.argmax(data[:, 3])][0]
    
    return beg, med, adv, beg_idx, med_idx, adv_idx

