import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CsvReader('/src/subtraction.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['value1'], row['value2'], row['result']))
            self.assertEqual(self.calculator.result, row['result'])

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
