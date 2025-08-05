# DSC 510
# Week 9
# Programming Assignment Week 9
# Author Peter Lozano
# 08/07/2025
# ####################### Assignment Details ###########################
# This program is a simple cash register
# 1. It requests for the user to input the price of an item.
# 2. It will allow the user to input as many item prices
#   as the user will like.
# 3. It will sum up the total as the user goes along adding
#   items to the simple cash register.
# 4. When the user is done, it will prompt the user with
#   a receipt containing the total price and the number
#   of items in the cart

import os
import locale

class CashRegister:
    """
    This class simulates a cash register by keeping track of the total price
    and the number of items added. It provides methods to add items and
    retrieve the current totals.
    """

    def __init__(self):
        """
        Constructor for the CashRegister class.
        Initializes the total price and item count to zero.
        """
        self.total_price = 0.0
        self.item_count = 0

    def add_item(self, price):
        """
        Adds an item to the register.

        :parameters:
            price (float): The price of the item to be added.
        """
        self.total_price += price
        self.item_count += 1
        print(f"Item added. Current subtotal: {locale.currency(self.total_price)}")

    @property
    def get_total(self):
        """
        Getter method for the total price.

        :returns:
            float: The current total price of all items.
        """
        return self.total_price

    @property
    def get_count(self):
        """
        Getter method for the item count.

        :returns:
            int: The total number of items added.
        """
        return self.item_count


def main():
    """
    Main function to run the cash register program.
    """
    # Set Locale for Currency Formatting
    # Using 'en_US.UTF-8' for standard US currency format.

    # Welcome message with assignment name
    print(f'Running: \'{os.path.basename(__file__)}\'\n')

    try:
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    except locale.Error:
        print("Warning: 'en_US.UTF-8' locale not supported. "
              "Using default system locale."
        )
        locale.setlocale(locale.LC_ALL, '')


    # --- Welcome Message ---
    print("=" * 50)
    print("      Welcome to the Simple Cash Register!")
    print("=" * 50)

    # --- Create an instance of the CashRegister ---
    register = CashRegister()

    # --- Main Program Loop ---
    while True:
        user_input = input("\nEnter the price of the item, "
                           "or type 'done' to finish: "
        ).strip().lower()

        if user_input == 'done':
            break

        try:
            item_price = float(user_input)
            if item_price < 0:
                print("Invalid input: Price cannot be negative. "
                      "Please try again."
                )
                continue
            register.add_item(item_price)
        except ValueError:
            print("Invalid input: "
                  "Please enter a valid number for the price."
            )

    # --- Display Final Totals ---
    total_items = register.get_count
    total_cost = register.get_total

    print("\n" + "-" * 50)
    print("                Transaction Complete")
    print("-" * 50)
    print(f"\nTotal number of items in the cart: {total_items}")
    # Use locale.currency to format the output
    print(f"Total amount of the cart: {locale.currency(total_cost)}")
    print("\nThank you for using the cash register!")


# --- Call to Main ---
if __name__ == "__main__":
    main()