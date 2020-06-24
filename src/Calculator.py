class Calculator:
    result = 0

    def __init__(self):
        pass

    @staticmethod
    def subtraction(a, b):
        return int(b) - int(a)

    @staticmethod
    def addition(a, b):
        return int(a) + int(b)

    @staticmethod
    def multiplication(a, b):
        return int(a) * int(b)

    @staticmethod
    def squaring(a):
        return int(a) * int(a)

    def subtract(self, a, b):
        self.result = Calculator.subtraction(a, b)
        return self.result

    def add(self, a, b):
        self.result = Calculator.addition(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Calculator.multiplication(a, b)
        return self.result

    def square(self, a):
        self.result = Calculator.squarify(a)
        return self.result