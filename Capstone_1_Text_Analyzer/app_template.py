# Capstone 1: Smart Text & Anagram Analyzer (Template Version)

import string

def clean_text(text):
    """
    TODO: Remove all punctuation from the text and convert it to lowercase.
    Hint: Use string.punctuation and the .replace() method.
    """
    pass

def count_words(text):
    """
    TODO: Return the total number of words in the text.
    Hint: Use the .split() method.
    """
    pass

def is_anagram(s1, s2):
    """
    TODO: Check if two strings are anagrams.
    Remember to ignore spaces and character casing!
    """
    pass

def recursive_anagram_guess(target_word, attempts_left):
    """
    TODO: Write a recursive function that prompts the user to guess an anagram.
    If they guess wrong, call the function again with attempts_left - 1.
    If attempts_left hits 0, the game is over (Base Case).
    """
    pass

def main_menu():
    """
    TODO: Create a while loop that displays a menu to the user.
    Take their input and call the appropriate functions above based on their choice.
    """
    pass

if __name__ == "__main__":
    main_menu()
