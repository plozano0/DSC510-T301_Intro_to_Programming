# DSC 510
# Week 9
# Programming Assignment Week 9
# Author Peter Lozano
# 07/30/2025
# ####################### Assignment Details ###########################
# This program generates a Chuck Norris joke using an API.
# 1. It defaults using the dev category but allows the user
#   to select a category of their choosing.
# 2. This will allow the user to request for as many jokes
#   as they would like.

import os
import requests

def get_joke_categories():
    """
    Fetches the list of available joke categories from the API.

    :Returns:
        list: A list of strings, where each string is a category name.
              Returns None if the request fails.
    """
    api_url = "https://api.chucknorris.io/jokes/categories"
    try:
        response = requests.get(api_url, timeout=10)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"\nError: Could not fetch joke categories. "
              f"Please check your internet connection."
        )
        print(f"Details: {e}")
        return None

def get_joke(category):
    """
    Fetches a random joke from the specified category.

    :parameter:
        category (str): The category of joke to fetch.

    :Returns:
        str: The joke text (the "value" from the JSON response).
             Returns None if the request fails.
    """
    # Base URL for fetching a random joke
    api_url = ("https://api.chucknorris.io/jokes/random?"
               f"category={category}"
    )
    try:
        # Make the GET request with a timeout of 10 seconds
        response = requests.get(api_url, timeout=10)
        # Raise an exception if the request returned an HTTP error
        response.raise_for_status()

        # Parse the JSON response
        json_data = response.json()

        # Extract the joke value
        return json_data.get("value")

    except requests.exceptions.HTTPError as e:
        print(f"\nError: An HTTP error occurred: {e}")
        return None
    except requests.exceptions.ConnectionError as e:
        print("\nError: A connection error occurred. "
              f"Please check your network. {e}"
        )
        return None
    except requests.exceptions.Timeout as e:
        print(f"\nError: The request timed out. "
              f"The server might be busy. {e}"
        )
        return None
    except requests.exceptions.RequestException as e:
        # This is a catch-all for any other request-related exceptions
        print(f"\nAn unexpected error occurred: {e}")
        return None
    except ValueError:
        # Catches JSON decoding errors
        print("\nError: Failed to decode the JSON response "
              "from the server."
        )
        return None


def main():
    """
    Main function to run the joke generator program.
    """
    # Welcome message with assignment name
    print(f'Running: \'{os.path.basename(__file__)}\'\n')

    # --- Welcome Message ---
    print("=" * 50)
    print("   Welcome to the Chuck Norris Joke Generator!")
    print("=" * 50)
    print("\nThis program will fetch a random developer-themed "
          "joke for you."
    )

    # --- Fetch and display categories ---
    print("\nFetching available joke categories...")
    categories = get_joke_categories()

    # If categories couldn't be fetched, exit gracefully.
    if not categories:
        print("\nExiting program as we could not retrieve "
              "joke categories."
        )
        return

    # --- Main Program Loop ---
    while True:
        # --- User Category Selection ---
        print("\nAvailable Categories:")
        # Print categories in a neat format
        for i, cat in enumerate(categories):
            print(f"  { i +1}. {cat}")

        print("\nPlease select a category by name or number.")
        user_input = input("Press Enter to default to 'dev', "
                           "or enter your choice: "
        ).strip().lower()

        selected_category = ""
        # Default to 'dev' if the user just presses Enter
        if not user_input:
            selected_category = 'dev'
            print("Defaulting to 'dev' category.")
        # Check if the user entered a number
        elif user_input.isdigit():
            choice_index = int(user_input) - 1
            if 0 <= choice_index < len(categories):
                selected_category = categories[choice_index]
            else:
                print("Invalid number. Please try again.")
                continue
        # Check if the user entered a valid category name
        elif user_input in categories:
            selected_category = user_input
        else:
            print("Invalid category name. Please try again.")
            continue

        print("\nFetching a joke from the "
              f"'{selected_category}' category..."
        )

        # --- Get and Print Joke ---
        joke = get_joke(selected_category)
        if joke:
            print("\n" + "-" * 50)
            print("Here is your joke:")
            print(f"\n  \" {joke} \"")
            print("-" * 50)
        else:
            # Error messages are printed within the get_joke function
            print("Could not retrieve a joke at this time.")

        # --- Ask to Continue ---
        print("\nWould you like to get another joke?")
        another = input("Enter 'y' or 'yes' to continue, "
                        "or any other key to exit: "
        )

        # Normalize the input to lowercase and remove
        #   leading/trailing whitespace
        if another.lower().strip() not in ['y', 'yes']:
            break  # Exit the while loop

    print("\nThanks for using the Chuck Norris Joke Generator. "
          "Goodbye!"
    )


# --- Call to Main ---
if __name__ == "__main__":
    main()