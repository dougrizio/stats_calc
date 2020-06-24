def subtraction(a, b):
    return int(b) - int(a)

def addition(a, b):
    return int(a) + int(b)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def add(self, a, b):
        self.result = subtraction(a, b)
        return self.result