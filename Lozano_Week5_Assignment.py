# DSC 510
# Week 5
# Programming Assignment Week 5
# Author Peter Lozano
# 07/01/2025
# ######################## Assignment Details ##########################
# Purpose of program:
# 1. Program is to perform various calculations.
# 2. Program should include a variety of loops and functions.
# 3. Program will add, subtract, multiply, divide 2 numbers and
# provide average
# of multiple numbers from the input of the user.
# 4. Define function named perform_calculation and pass 1 parameter.
#    4a. This function will take 2 inputs from user and returns
#    a legible and contextual format for the user.
# 5. Define function named calculate_average that takes no parameters.
#    5a. This function will ask how many numbers they wish to input.
#    5b. Function will use the number entered for the count of loops
#    5c. Within the function it must prompt user to input numbers
#    in the amount that was given prior to calculate total and average.
#    5d. The function will return the average in legible and
#    contextual format for the user.

import locale
import os
locale.setlocale(locale.LC_ALL, '')

def perform_calculation(operation):
    """
    Prompts the user for two numbers and performs a specified calculation.

    This function handles user input for two numbers and includes error handling
    for non-numeric input and division by zero.

    :param:
        operation (str): The mathematical operation to perform ('+', '-', '*', '/').

    :returns:
        float: The result of the calculation. Returns None if an error occurs.
    """
    try:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))

        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            # A specific try block for the division operation
            try:
                return num1 / num2
            except ZeroDivisionError:
                print("\nError: Cannot divide by zero. Please try again.")
                return None
        return None
    except ValueError:
        print('\nThe value entered is not a number. '
                'Please enter valid number for calculation.'
        )
        return None

def calculate_average():
    """
    Calculates the average of a series of numbers provided by the user.

    This function first asks how many numbers will be entered and then uses a
    for loop to gather the numbers. Includes error handling for all inputs.

    Returns:
        float: The average of the numbers. Returns None if an error occurs.
    """
    try:
        count = int(input("How many numbers do you wish to average? "))
        if count <= 0:
            print("\nError: Number of values must be greater than zero.")
            return None
    except ValueError:
        print("\nError: Please enter a valid whole number for the count.")
        return None

    total = 0.0
    for i in range(count):
        while True: # Loop to ensure valid input for each number
            try:
                num = float(input(f"Enter number {i + 1}: "))
                total += num
                break # Exit the inner while loop on successful input
            except ValueError:
                print('\nThe value entered is not a number. '
                      'Please enter valid number for calculation.'
                )
                # The loop will continue, asking for the same number again.

    return total / count

def main():
    """
    The main driver of the program,
    containing the primary user interaction loop.
    """
    print(f'Welcome to \'{os.path.basename(__file__)}\'')

    while True:
        # Prompt the user for the desired operation
        print("\nPlease select an operation:")
        print("  'calc'    - Perform a calculation (+, -, *, /)")
        print("  'average' - Calculate the average of multiple numbers")
        print("  'quit'    - Exit the program")
        user_choice = input("Enter your choice: ").lower()

        # Evaluate the user's choice using if/elif/else statements
        if user_choice == 'calc':
            op_choice = input("Enter the operation (+, -, *, /): ")
            if op_choice in ['+', '-', '*', '/']:
                result = perform_calculation(op_choice)
                if result is not None:
                    print("\nThe result of the calculation is: "
                          f"{locale.format_string(
                            "%.2f"
                            , result
                            , grouping=True
                            )
                          }"
                    )
            else:
                print("\nInvalid operation selected. "
                      "Please choose from +, -, *, /."
                )

        elif user_choice == 'average':
            average = calculate_average()
            if average is not None:
                print(f"\nThe calculated average is: "
                      f"{locale.format_string(
                          "%.2f"
                          , average
                          , grouping=True
                          )
                      }"
                )

        elif user_choice == 'quit':
            print("\nThank you for using the calculator. Goodbye!")
            break  # Exit the while loop

        else:
            print("\nInvalid choice. "
                  "Please enter 'calc', 'average', or 'quit'."
            )

if __name__ == '__main__':
    main()