# Finding Expression with decimal numbers line  #
# Module: expression_finder.py                  #
# Version: 1.0                                  #
# Author: Sergey Patokin                        #
# Last Update: 02.13.2024                       #
# Author URL: https://sergeyforever.online/     #

from itertools import product  # Import the product function from the itertools module

def find_expressions(total):
    operators = ['+', '-', ''] # Generate a sequence from 9 to 0 (inclusive)
    digits = range(9, -1, -1)
    expressions = []  # Initialize an empty list to store found expressions
    for ops in product(operators, repeat=len(digits) - 1):
        # Construct the expression by joining each digit with its corresponding operator
        expression = ''.join(str(d) + op for d, op in zip(digits, ops)) + str(digits[-1])
        # If the result of the expression equals the specified total, add it to the list
        if eval(expression) == total:
            expressions.append(expression)
    return expressions  # Return the list of found expressions

target_total = 200 # Set the target result
expressions = find_expressions(target_total)
# Print the result: the found expressions if they exist, otherwise indicate that no solution was found
if expressions:
    print("Found expressions:")
    for expression in expressions:
        print(f"{expression}={target_total}")
else:
    print("No solution found.")

