import numpy as np

#read a CSV file and return it as a 2D numpy array
def read_csv(file_name, header):
    fname = f'{file_name}.csv'
    array = np.genfromtxt((open(fname)), delimiter = ",", dtype = None, skip_header = header,)       #Make 4 CSV lists with floats and data separated       
    return array



def write_csv(numpy_array):
    open(numpy_array).write

print('Hello World!')




