FROM python:3

ADD tests /tests

CMD [ "python", "./tests/CalculatorTests.py" ]