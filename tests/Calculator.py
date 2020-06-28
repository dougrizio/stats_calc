import math

class Calculator:
    result = 0

    def __init__(self):
        pass

    @staticmethod
    def addition(a, b):
        return int(a) + int(b)

    @staticmethod
    def subtraction(a, b):
        return int(b) - int(a)

    @staticmethod
    def multiplication(a, b):
        return int(a) * int(b)

    @staticmethod
    def division(a, b):
        return float(b) / float(a)

    @staticmethod
    def squaring(a):
        return int(a) * int(a)

    @staticmethod
    def squarerooting(a):
        return math.sqrt(float(a))

    def add(self, a, b):
        self.result = Calculator.addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = Calculator.subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Calculator.multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = Calculator.division(a, b)
        return self.result

    def square(self, a):
        self.result = Calculator.squaring(a)
        return self.result

    def squareroot(self, a):
        self.result = Calculator.squarerooting(a)
        return self.result