# DSC 510
# Week 8
# Programming Assignment Week 8
# Author Peter Lozano
# 07/26/2025
# ####################### Assignment Details ###########################
# This program analyzes the "Gettysburg Address" text file.
# It calculates the frequency of each unique word and outputs the
# results to a new text file specified by the user.
#
# Key features:
# 1. Reads from 'gettysburg.txt'.
# 2. Processes the text to count unique words,
#       ignoring case and punctuation.
# 3. Prompts the user for an output filename.
# 4. Writes the total count of unique words to the new file.
# 5. Appends a formatted table of each word and its count
#       to the same file.
# 6. Uses functions for clarity: add_word, process_line,
#       and process_file.
# 7. Includes try-except blocks for file handling.

import os
import string


def add_word(word, word_counts):
    """
    Adds a word to the dictionary or increments its count if
        it already exists.

    :parameters:
        word (str): The word to add to the dictionary.
        word_counts (dict): The dictionary of word counts.
    """
    # Ensure the word is not an empty string before processing.
    if word:
        word_counts[word] = word_counts.get(word, 0) + 1


def process_line(line, word_counts):
    """
    Processes a single line of text to count the words.
    It converts the line to lowercase, removes punctuation and
    em-dashes,
    and splits it into individual words.

    :parameters:
        line (str): The line of text to process.
        word_counts (dict): The dictionary of word counts to update.
    """
    # Convert the entire line to lowercase for case-sensitive counting.
    line = line.lower()
    # Replace em-dashes with spaces to properly separate words.
    line = line.replace('—', ' ')
    # Remove all standard punctuation characters from the line.
    line = line.translate(str.maketrans('', '', string.punctuation))

    # Split the cleaned line into a list of words.
    words = line.split()

    # Add each word from the list to the dictionary.
    for word in words:
        add_word(word, word_counts)


def process_file(word_counts, filename):
    """
    Writes the formatted word counts to the specified file.
    The words are sorted by frequency in descending order. This function
    appends to the file, assuming it has already been created.

    :parameters:
        word_counts (dict): The dictionary of word counts.
        filename (str): The name of the file to write the output to.
    """
    try:
        # Open the specified file in append mode ('a') to add to it.
        with open(filename, 'a') as file:
            file.write(
                f"\n{'#' * 10} Word Frequency Analysis {'#' * 10}\n"
            )

            # Sort the dictionary items by count
            # (the second element, x[1])
            # in descending order.
            sorted_word_counts = sorted(
                word_counts.items(),
                # e.g., (four | 12 <-- sorting here)
                key=lambda x: x[1],
                reverse=True
            )

            # Write the header for the word count table to the file.
            file.write(f"\n{'Word':<15} | {'Count'}\n")
            file.write("-" * 23 + "\n")

            # Write each word and its count to the file.
            for word, count in sorted_word_counts:
                file.write(f"{word:<15} | {count}\n")
    except Exception as e:
        # Catch and report any errors that occur during file writing.
        print(f"Error: Could not write to the file '{filename}'.")
        print(e)


def main():
    """
    Main function to orchestrate the file processing.
    It reads the source file, processes its content, and then
    writes the analysis to a user-specified output file.
    """

    # Welcome message with assignment name
    print(f'Welcome to \'{os.path.basename(__file__)}\'\n')

    word_counts = {}
    original_file_directory = ""  # Store the directory of the original file

    # Continuously ask for file path until a valid one is provided
    while True:
        try:
            file_path = input(
                "Please enter your full path of the file you want analyzed:\n"
            )
            with open(file_path, 'r') as fileHandle:
                # Store the directory of the original file
                original_file_directory = os.path.dirname(file_path)
                for line in fileHandle:
                    process_line(line, word_counts)
            break  # Break the loop if file is opened successfully
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            print("Please make sure the file path is correct.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Prompt the user to enter a name for the output file.
    output_filename_base = input("Please enter the filename for the output "
                                 "(e.g., output.txt): "
                                 )

    # Construct the full path for the output file
    # If the original_file_directory is empty
    # then os.path.join will return the original directory.
    output_filename = os.path.join(
        original_file_directory
        , output_filename_base
    )

    # Use a try-except block for writing the initial part of the file.
    try:
        # Open the user-specified file in write mode ('w').
        # This will create the file or overwrite it if
        # it already exists.
        with open(output_filename, 'w') as file:
            file.write(f"Number of unique words: {len(word_counts)}\n")
    except Exception as e:
        print(
            f"Error: Could not create or write to the file "
            f"'{output_filename}'."
        )
        print("Please check permissions and the filename.")
        print(e)
        return  # Exit if the file cannot be created.

    # Call the process_file function to append the detailed word list.
    process_file(word_counts, output_filename)

    print(
        f"\nProcessing complete. The analysis has been saved to "
        f"'{output_filename}'."
    )


# This check ensures the main function is called only when the script is executed directly.
if __name__ == "__main__":
    main()