# DSC 510
# Week 3
# Programming Assignment Week 3
# Author Peter Lozano
# 06/17/2025
################################################### Assignment Details #############################################
# Purpose of program:
# 1. Print welcome statement for user.
# 2. Retrieve company name.
# 3. Retrieve number of feet of fiber optic cable needed
# to be installed from user.
# 4. Calculate the installation of fiber optic cable by
# multiplying number of feet by a conditional statement
#       4a. If feet entered <= 100. Multiply feet by $.95
#       4b. If feet entered > 100 & feet <= 250. Multiply feet by $.85
#       4c. If feet entered > 250 & feet <= 500. Multiply feet by $.75
#       4d. If feet entered > 500. Multiply feet by $.55
# 5. Print receipt of user including company name, number of feet requested,
# and total cost in legible format.

import os
from datetime import date
import locale
locale.setlocale(locale.LC_ALL, '')

# Requesting user input to let us properly welcome them.
print(f'Welcome to \'{os.path.basename(__file__)}\'')
user_name = input("Please tell me your name?\n")
print(f"Welcome {user_name}! We aim to provide you the best fiber optic "
      f"cables at the best price guaranteed!")

# Requesting user to provide us the company name for receipt purposes.
company_name = input("What is the name of your company?\n")

# Require input from user to enter desired number of feet for calculation.
def get_amount_requested(prompt):
    """
    Ensures user input is a valid float/number for calculation.
    :param: prompt: Message for prompt to display to user.
    :return: user_input ==> float
    """
    while True:
        try:
            user_input = input(prompt)
            return float(user_input)

        except ValueError:
            print(f'The value entered is not a number.'
                ' Please enter valid number for calculation.')


number_of_feet = get_amount_requested("To calculate total cost,\n"
                                      "Please enter the number (in feet) how much "
                                      "fiber optic cable is needed?\n"
                                      "Enter your number here: "
                                      )

# Creating variables to calculate the total cost.
# cost_per_foot = 0.95
def cost_calculator(amount_requested, cost_per_foot= 0.95):
    """
    Provides the total cost per foot of fiber optic cable
    with the standard/discount applied.
    :param amount_requested: The amount in feet for fiber optic cable.
    :param cost_per_foot: The standard {0.95} /
    discount cost per foot depending on amount requested.
    :return: total_cost ==> float, cost_per_foot ==> float
    """
    try:
        if amount_requested <= 100:  # First condition
            # Multiplies based on default cost
            total_cost = amount_requested * cost_per_foot
            return total_cost, cost_per_foot
        elif 100 < amount_requested <= 250:  # Second condition if met
            # cost_per_foot changes due to amount_requested
            cost_per_foot = 0.85
            total_cost = amount_requested * cost_per_foot
            return total_cost, cost_per_foot
        elif 250 < amount_requested <= 500:  # Third condition if met
            cost_per_foot = 0.75
            total_cost = amount_requested * cost_per_foot
            return total_cost, cost_per_foot
        else:  # All other conditions should fall into this condition
            cost_per_foot = 0.55
            total_cost = amount_requested * cost_per_foot
            return total_cost, cost_per_foot
    # Exception will trigger when a non-numeric value is entered.
    except Exception as e:
        print(f'Exception {e} has occurred. Please enter valid number for calculation.')
        return None

# Initializing the cost_calculator function
cost_calculator(number_of_feet)

# Receipt is printed for user.
print("%.2f"% number_of_feet)
print(f"Thank you {user_name}!\n"
      "Here is your receipt:\n"
      f"{'#' * 20} Receipt {'#' * 20}\n"
      f"Date: {date.today().strftime("%m/%d/%Y")}\n"
      f"Company Name: {company_name}\n"
      "Fiber optic cable ordered: "
      f"{locale.format_string("%.2f", number_of_feet, grouping=True)} feet.\n"
      "Cost per foot: "
      f"{locale.currency(cost_calculator(number_of_feet)[1], grouping=True)}\n"
      "Total Cost: "
      f"{locale.currency(cost_calculator(number_of_feet)[0], grouping=True)}\n"
      f"{'#' * 22} End {'#' * 22}\n"
)
