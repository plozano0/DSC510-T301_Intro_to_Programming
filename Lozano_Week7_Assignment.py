# DSC 510
# Week 7
# Programming Assignment Week 7
# Author Peter Lozano
# 07/16/2025
# ####################### Assignment Details ###########################
# Purpose of program:
# 1. Program will return unique word count based on provided text file.
# 2. Program will remove punctuation from words and convert the words.
# to a common case, and remove any whitespace.
# 3. Program should contain 4 main functions:
#    3a. add_word - adds each word in file.
#    3b. process_line - convert words to common case.
#    3c. pretty_print - prints the results in a legible format.
import os
import string

def add_word(word, word_counts):
    """
    Summary
    Adds a word to the dictionary or increments its count
    if it already exists.

    :parameters:
        word (str): The word to add to the dictionary.
        word_counts (dict): The dictionary of word counts.
    """
    if word:  # Ensure the word is not an empty string
        word_counts[word] = word_counts.get(word, 0) + 1

def process_line(line, word_counts):
    """
    Summary
    Processes a single line of text to count the words.
    It converts the line to lowercase, removes punctuation and
    em-dashes, and splits it into words.

    :parameters:
        line (str): The line of text to process.
        word_counts (dict): The dictionary of word counts to update.
    """
    # Convert the line to lowercase
    line = line.lower()

    # Replace em-dashes (—) with spaces to handle cases
    #   like "dedicate—we"
    line = line.replace('—', ' ')

    # Remove punctuation from the line
    # string.punctuation is a pre-initialized string giving the
    #   punctuation characters
    # The str.translate() method returns a copy of the string in which
    #   all characters have been translated using the given
    #   translation table
    line = line.translate(str.maketrans('', '', string.punctuation))

    # Split the line into a list of words
    words = line.split()

    # Add each word to the dictionary
    for word in words:
        add_word(word, word_counts)

def pretty_print(word_counts):
    """
    Summary
    Prints the word counts in a nicely formatted table,
    sorted by frequency.

    :parameter:
        word_counts (dict): The dictionary of word counts.
    """
    print(f"\n{'#' * 10} "
          "Word Frequency Analysis of the Gettysburg Address "
          f"{'#' * 10}"
    )
    # sorted() returns a sorted list of the specified iterable object.
    # We sort by the second element of the tuple (the count) in
    #   descending order.
    # dict.items() returns a view object that displays a list of a given
    #   dictionary's key-value tuple pair.
    # The lambda function specifies that we sort by the value (x[1]).
    sorted_word_counts = sorted(
        word_counts.items()
        # e.g., (four | 12 <-- sorting here)
        , key=lambda x: x[1]
        , reverse=True
    )

    # Print header for the table
    print(f"\n{'Word':<15} | {'Count'}")
    print("-" * 23)

    # Print each word and its count
    for word, count in sorted_word_counts:
        print(f"{word:<15} | {count}")

def main():
    """
    Summary
    Main function is to processes the inputted text
    and prints the results. The function will return
    the total count of words within the file and
    the unique counts of words within the text file
    :parameter:
        fileHandle: The text file being processed
    :return:
        length_of_dict ==> int, word_counts ==> int
    """
    # Welcome message with assignment name
    print(f'Welcome to \'{os.path.basename(__file__)}\'\n')

    # The text of the Gettysburg Address
    word_counts = {}
    file_path = ''
    while not os.path.exists(file_path):
        try:
            file_path = input("Please enter the full path to the text file: ")
            with open(file_path, 'r') as fileHandle:
                for line in fileHandle:
                    process_line(line, word_counts)
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found. Please try again.")
        except IOError as e:
            print(f"Error reading file: {e}. Please check permissions or file integrity.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Split the text into lines
    lines = word_counts

    # Process each line
    for line in lines:
        process_line(line, word_counts)

    # Print the final results
    pretty_print(word_counts)

if __name__ == "__main__":
    main()