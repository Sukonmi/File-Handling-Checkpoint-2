# 1. Create a new file called "calculator_2.0.py"

# 2. Create a class called "Calculator" that contains the following:
# A dictionary attribute to store the available mathematical operations and their corresponding functions
# A method called "init" that initializes the dictionary with the basic mathematical operations (+, -, *, /) and corresponding functions
# A method called "add_operation" that takes in two arguments: the operation symbol and the corresponding function. This method should add the new operation and function to the dictionary.
# A method called "calculate" that takes in three arguments: the first number, the operation symbol, and the second number. This method should use the dictionary to determine the appropriate function to perform the calculation. It should also include error handling to check if the operation symbol is valid and if the input values are numbers. If an error is encountered, the method should print an error message and raise an exception.

class Calculator:
    def __init__(self, operations = None):
        self.operations = operations or {}
        self.init()

    def init(self):
        self.operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"

    def add_operation(self, symbol, function):
        self.operations[symbol] = function
