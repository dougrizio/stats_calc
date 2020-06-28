FROM python:3

ADD tests /test

CMD [ "python", "./tests/CalculatorTests.py" ]