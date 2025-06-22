# DSC 510
# Week 6
# Programming Assignment Week 6
# Author Peter Lozano
# 07/08/2025
# ######################## Assignment Details #############################
# Purpose of program:
# 1. Program is to perform various calculations.
# 2. Program should include a variety of loops and functions.
# 3. Program will add, subtract, multiply, divide 2 numbers and provide average
# of multiple numbers from the input of the user.
# 4. Define function named perform_calculation and pass 1 parameter.
#    4a. This function will take 2 inputs from user and returns a legible and
#    contextual format for the user.
# 5. Define function named calculate_average that takes no parameters.
#    5a. This function will ask user how many numbers they wish to input.
#    5b. Function will use the number entered for the count of loops
#    5c. Within the function it must prompt user to input numbers
#    in the amount that was given prior to calculate total and average.
#    5d. The function will return the average in legible and contextual format
#    for the user.

import locale
import os
locale.setlocale(locale.LC_ALL, '')

def main():
    """
    Summary
    Main function of program is to prompt user to enter a number of
    temperatures indefinitely. It will accept a sentinel value that
    will stop user input. The function will return the min/max
    of temperatures and the number of temperatures entered.
    :return: largest_temp ==> float, smallest_temp ==> float,
    num_temperatures ==> integer
    """
    print(f'Welcome to \'{os.path.basename(__file__)}\'')

    temperatures = []

    print(f"{'#' * 22} Temperature Analysis Program {'#' * 22}")
    print('Enter a series of temperatures (e.g., 98.6, 72, 32).')
    print('Type \'done\' when you are finished.')
    # print('#' * 77)

    # Loop indefinitely to collect user input.

    while True:
        # Prompt the user to input a temperature.
        user_input = input('Enter a temperature (or \'done\' to finish): ')

        # The value 'done' will stop the user input loop.
        if user_input.lower() == 'done':
            break # Exiting loop

        # A try block to prevent unhandled exceptions for non-numeric input.
        try:
            # Convert the user's input to a float type.
            temp = float(user_input)
            # Add the valid temperature to our list.
            temperatures.append(temp)
        except ValueError:
            # If the input is not a valid number, inform the user and continue.
            print('Invalid input. Please enter a valid number or \'done\'.')

    # After the loop, check if any temperatures were actually entered.
    if temperatures:
        # Evaluate the temperatures list to determine the largets and smallest.
        largest_temp = max(temperatures)
        smallest_temp = min(temperatures)

        # Determine the number of temperatures entered by the user.
        num_temperatures = len(temperatures)

        print('#' * 28 + ' Analysis Complete ' + '#' * 28)

        # Print message telling the user how many temperatures were entered.
        print(f'You entered a total of {num_temperatures} temperatures.')

        # Print the largest temperature in a legible format.
        print(f'Largest temperature entered: {largest_temp}°')

        # Print the smallest temperature in a legible format.
        print(f'Smallest temperature entered: {smallest_temp}°')

        print('#' * 75)
    else:
        # If the list is empty, print a message indicating that.
        print('No temperatures were entered. The program will now exit.')

# Standard entry point for a Python script
if __name__ == '__main__':
    main()