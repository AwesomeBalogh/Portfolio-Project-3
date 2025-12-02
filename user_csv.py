import numpy as np
#read a CSV file and return it as a 2D numpy array
def read_csv(file_name, header):
    '''
    Take a CSV file and convert it into a 2D numpy array
    Inputs: file name, header status
    Outputs: numpy array of data
    '''
    fname = f'{file_name}.csv'
    array = np.genfromtxt((open(fname)), delimiter = ",", dtype = None, skip_header = header,)       #Make CSV numpy arrays (0 to include header, 1 to skip header)      
    return array


def write_csv(file_name, numpy_array, overwrite):       #for overwrite, input 'x' to make a new file, input 'a' to append 
    '''
    Format and write a CSV file from a numpy array

    Inputs: file name, array to be made into a CSV file, overwrite operator

    Returns: None
    '''
    with open(str(file_name) + '.csv', str(overwrite)) as file:     #used with operator to ensure safe file creation

        for i in range(len(numpy_array)):                           #generate row of data for the CSV file
            row = ''
            for j in range(len(numpy_array[i])):                    #itterate through each index of the file and format it correctly
                row += str(numpy_array[i][j]) + ','

    
            file.write(row + '\n')                                  #write one row of the file, then make a new line to make columns
    print(f'{file_name} created sucessfuly')        

