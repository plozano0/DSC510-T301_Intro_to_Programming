# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Peter Lozano
# 06/07/2025
################################################### Assignment Details #############################################
# Purpose of program:
# 1. Print welcome statement for user.
# 2. Retrieve company name.
# 3. Retrieve number of feet of fiber optic cable needed to be installed from user.
# 4. Calculate the installation of fiber optic cable by multiplying number of feet by $.95
# 5. Print receipt of user including company name, number of feet requested, and total cost in legible format.

import locale
locale.setlocale(locale.LC_ALL, '')

# Requesting user input to let us properly welcome them.
user_name = input("Please tell me your name?\n")
print(f"Welcome {user_name}!")

# Requesting user to provide us the company name for receipt purposes.
company_name = input("What is the name of your company?\n")

# Require input from user to enter desired number of feet for calculation.
number_of_feet = float(input("To calculate total cost,\n"
                        "Please enter the number (in feet) how much fiber optic cable is needed?")
)

# Creating variables to calculate the total cost.
cost_per_foot = 0.95
total_cost = (number_of_feet * cost_per_foot)

# Receipt is printed for user.
print("%.2f"% number_of_feet)
print(f"Thank you {user_name}!\n"
      f"Cost per foot is {locale.currency(cost_per_foot)}\n"
      f"{company_name}'s total cost is {locale.currency(total_cost)} for {"%.2f" % number_of_feet} feet."
)
