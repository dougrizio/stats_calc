FROM python:3

ADD Tests /Tests

CMD [ "python", "./Tests/CalculatorTests.py" ]