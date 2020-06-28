import csv
import unittest
from Calculator import Calculator
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    def test_addition(self):
        test_addition_data = MyTestCase.CsvReader('/Tests/ut_addition.csv')
        pprint(test_addition_data)
        for row in test_addition_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_division(self):
        test_division_data = MyTestCase.CsvReader('/Tests/ut_division.csv')
        pprint(test_division_data)
        for row in test_division_data:
            self.assertAlmostEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

    @staticmethod
    def CsvReader(filepath):
        objects = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                objects.append(row)
        return objects

if __name__ == '__main__':
    unittest.main()