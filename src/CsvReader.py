import csv
from pprint import pprint

class MyTestCase(unittest.TestCase):
    @staticmethod
    def CsvReader(filepath):
        objects = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                objects.append(row)
        return objects