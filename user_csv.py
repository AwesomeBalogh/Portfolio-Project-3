import numpy as np
#read a CSV file and return it as a 2D numpy array
def read_csv(file_name, header):
    '''
    Take a CSV file and convert it into a 2D numpy array

    Param: file name, header status(0 to include header, 1 to exclude header)

    Return: numpy array of data
    '''

    header = int(header)            #ensure header is an int value
    
    if (header == 0 or header == 1):
        fname = f'{file_name}.csv'

        raw_csv = open(fname, 'r', newline = '').read().strip().split('\r\n')       #read the csv, then remove extra whitespace, and split it by the new lines
    
        refined_csv = []

        int_char = ['.','0','1','2','3','4','5','6','7','8','9']

        for i in range(len(raw_csv)- header):       #for every string from splitting by newline, split it further by the commas and append it to a new CSV
            row = (raw_csv[i + header].split(','))
            for j in range(len(row)):
                for z in range(len(int_char)):
                    if (str(int_char[z]) in str(row[j])):
                        row[j] = float(row[j])
                    

            refined_csv.append(row)                 #append each resorts row to a list

        arr = np.array(refined_csv, dtype = None)             #convert list to numpy array  

        return arr
        
    else:
        print('Error, please either input 0 to include header or 1 to remove headers')


def write_csv(file_name, numpy_array, overwrite):       #for overwrite, input 'x' to make a new file, input 'a' to append 
    '''
    Format and write a CSV file from a numpy array

    Params: file name, array to be made into a CSV file, overwrite operator, 'x' to maxe new file, 'a' to append

    Returns: None
    '''
    file = open(f'{file_name}.csv', str(overwrite))

    for i in range(len(numpy_array)):                           #generate row of data for the CSV file
        row = []
        for j in range(len(numpy_array[i])):                    #itterate through each index of the file and append it to the list
            row.append(str(numpy_array[i][j]))
        
        row = ",".join(row)         #join the elements of the list with a comma
        
        file.write(row)             #write to the new file
        
        file.write('\n')            #adds newline character at the end of the row
    
    print(f'{file_name} created sucessfuly')


#=================================================================================================================================================
#for testing only

#uncomment to test read.csv
#print(read_csv('resort runs', 1))



#uncomment to test write.csv()
#list = [['Paint Jars','Magnet Tiles','Legos'],[102,203,21],[123,34,21]]
#arr = np.array(list)
#write_csv('test',arr ,'x')