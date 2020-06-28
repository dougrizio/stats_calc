from Addition import addition
from Division import division

def mean(data):
    numValues = len(data)
    total = 0
    for num in data:
        total = addition(total, num)
    return division(total, numValues)