# Expression Finder

This Python script finds all possible expressions that combine digits from 9 to 0 using addition (+), subtraction (-), or no operation to yield a specified total.

## Usage

1. Make sure you have Python installed on your system.
2. Clone this repository or download the expression_finder.py file.
3. Run the script using Python:

    ```bash
    python expression_finder.py
    ```
    
4. The script will output all expressions that result in the desired total (if found), otherwise, it will indicate that no solution was found.

## Example

Target total: 200

Found expressions:
98+76-5+43-2-10=200
97+86-5+42-3-10=200
... (other expressions)
98-7+65+43+2-1-0=200

## How It Works

The script generates all possible combinations of addition, subtraction, and no operation between digits from 9 to 0 and evaluates each expression to find those that yield the specified total.
