from Calculator import Calculator
from Mean import mean
from Median import median
from Mode import mode

class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result

    def median(self):
        self.result = median(self.data)
        return self.result

    def mode(self):
        self.result = mode(self.data)
        return self.result