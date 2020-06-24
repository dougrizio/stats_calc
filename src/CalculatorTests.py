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

    def test_subtraction(self):
        test_subtraction_data = MyTestCase.CsvReader('/src/ut_subtraction.csv')
        pprint(test_subtraction_data)
        for row in test_subtraction_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_addition(self):
        test_addition_data = MyTestCase.CsvReader('/src/ut_addition.csv')
        pprint(test_addition_data)
        for row in test_addition_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    @staticmethod
    def CsvReader(filepath):
        data = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                data.append(row)

    def return_data_as_objects(self):
        objects = []
        for row in self:
            objects.append(MyTestCase.CsvReader)
        return objects

if __name__ == '__main__':
    unittest.main()