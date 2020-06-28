import math
from Addition import addition
from Division import division

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result