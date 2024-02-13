# Finding Expression with decimal numbers line  #
# Module: main.py                               #
# Version: 1.0                                  #
# Author: Sergey Patokin                        #
# Last Update: 02.13.2024                       #
# Author URL: https://sergeyforever.online/     #

from itertools import product  # Import the product function from the itertools module

def find_expression(total):
    operators = ['+', '-', '']  # Define possible operators: addition, subtraction, and empty operator (none)
    digits = range(9, -1, -1)  # Generate a sequence from 9 to 0 (inclusive)
    for ops in product(operators, repeat=len(digits) - 1):  # Iterate over all possible combinations of operators
        # Construct the expression by joining each digit with its corresponding operator
        expression = ''.join(str(d) + op for d, op in zip(digits, ops)) + str(digits[-1])
        # If the result of the expression equals the specified total, return the expression
        if eval(expression) == total:
            return expression
    return None  # If no expression yields the desired result, return None

target_total = 200  # Set the target result
expression = find_expression(target_total)  # Find an expression yielding this result
# Print the result: the found expression if it exists, otherwise indicate that no solution was found
print(f"Result: {expression}={target_total}" if expression else "No solution found.")
