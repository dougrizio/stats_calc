from Addition import addition
from Subtraction import subtraction
from Division import division

def median(data):
    numValues = len(data)
    data.sort()
    if numValues % 2 == 0:      #should probably find a way to obtain remainder using division method
        median1 = division(2, data[numValues])
        median2 = division(2, data[subtraction(1, numValues)])
        return division(2, (addition(median1, median2)))        #should we use mean method or leave as is?
    else:
        return data[division(2, numValues)]