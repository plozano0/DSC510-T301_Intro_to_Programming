# DSC 510
# Week 6
# Programming Assignment Week 6
# Author Peter Lozano
# 07/08/2025
# ####################### Assignment Details ###########################
# Purpose of program:
# 1. Program is to accept an indefinite number of temperatures.
# 2. Program should end user input based on sentinel value.
# 3. Program will return the max/min of temperatures entered.
# 4. Program will also return the number of temperatures in the list.
#    4a. All values return should be in legible format.

import locale
import os
locale.setlocale(locale.LC_ALL, '')


def to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def main():
    """
    Summary
    Main function of the program is to prompt user to enter a number of
    temperatures indefinitely. It will convert Fahrenheit to Celsius
    for comparison purposes. It will accept a sentinel value that
    will stop user input. The function will return the min/max
    of temperatures and the number of temperatures entered.
    :return: largest_temp ==> float, smallest_temp ==> float,
    num_temperatures ==> integer
    """

    # Welcome message with assignment name
    print(f'Welcome to \'{os.path.basename(__file__)}\'\n')

    # An empty list to store the temperatures entered by the user.
    # We will store everything in Celsius for consistent comparison.
    temperatures_celsius = []

    print(f"{'#' * 22} Temperature Analysis Program {'#' * 22}\n")
    print("Enter temperatures followed by their unit"
          "(C for Celsius, F for Fahrenheit).")
    print("For example: '100 F', '32 C', '212f', '0c'")
    print("Type 'done' when you are finished.\n")
    print('#' * 75 + '\n')

    # Loop indefinitely to collect user input.
    while True:
        # Prompt the user to input a temperature and its unit.
        user_input = input("Enter a temperature (e.g., '72 F')"
                           " or 'done' to finish: ").strip()

        # The sentinel value 'done' will stop the user input loop.
        if user_input.lower() == 'done':
            break  # Exit the loop

        # A try block to prevent unhandled exceptions for
        # bad input formats.
        try:
            # Split the input into the value and the unit.
            parts = user_input.split()
            if len(parts) != 2:
                # Handle cases like "100" or "100 F F"
                raise ValueError("Please enter both a number and a unit"
                                 " (C or F).")

            value_str, unit = parts
            value = float(value_str)
            unit = unit.upper()

            # Convert to Celsius for comparison purposes.
            if unit == 'C':
                temperatures_celsius.append(value)
            elif unit == 'F':
                celsius_temp = to_celsius(value)
                temperatures_celsius.append(celsius_temp)
            else:
                # Handle incorrect units like 'K' or 'X'
                print("Invalid unit. Please use 'C' for Celsius or"
                      " 'F' for Fahrenheit.")
                continue  # Skip to the next loop iteration

        except (ValueError, IndexError):
            # If the input is not a valid number or format,
            # inform the user and continue.
            print("Invalid input. Please enter in the format "
                  "'value unit' (e.g., '98.6 F').")

    # After the loop, check if any temperatures were actually entered.
    if temperatures_celsius:
        # Evaluate the list to determine the largest and
        # smallest in Celsius.
        largest_c = max(temperatures_celsius)
        smallest_c = min(temperatures_celsius)

        # Convert the results back to Fahrenheit for display.
        largest_f = to_fahrenheit(largest_c)
        smallest_f = to_fahrenheit(smallest_c)

        # Determine the number of temperatures entered.
        num_temperatures = len(temperatures_celsius)

        print("\n--- Analysis Complete ---")
        # Print the largest temperature in both formats.
        print(f"Largest temperature: "
              f"{largest_c:.2f}°C / {largest_f:.2f}°F"
        )
        # Print the smallest temperature in both formats.
        print(f"Smallest temperature: "
              f"{smallest_c:.2f}°C / {smallest_f:.2f}°F"
        )

        # Print a message that tells the user how many temperatures
        # are in the list.
        print("You entered a total of "
              f"{num_temperatures} temperatures."
        )
        print("-" * 30)
    else:
        # If the list is empty, print a message indicating that.
        print("\nNo temperatures were entered. "
              "The program will now exit."
        )


# Standard Python practice to call the main method.
if __name__ == "__main__":
    main()