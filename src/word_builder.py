"""
Module: word_builder
This module provides a function to construct a word by extracting specific letters
from a list of words.
"""


def construct_new_word(words):
    """
    Constructs a new word by concatenating the nth letter from each word in the list.

    Args:
        words (list): A list of words from which letters will be extracted.

    Returns:
        str: A word constructed by concatenating the selected letters.
    """

    try:
        # Check that the input is a list
        if not isinstance(words, list):
            raise TypeError("Input must be a list of words")

        # Check that the list is not empty
        if not words:
            raise ValueError("The list of words cannot be empty")

        # Check that all elements are strings
        if not all(isinstance(word, str) for word in words):
            raise TypeError("All elements must be strings")

        # Check that words are long enough
        if any(len(word) <= i for i, word in enumerate(words)):
            raise IndexError(
                "Some words are too short to extract the required letter")

        # Build the new word
        return ''.join(word[i] for i, word in enumerate(words))

    except TypeError as e:
        print(f"Type Error: {e}")
        return None
    except ValueError as e:
        print(f"Value Error: {e}")
        return None
    except IndexError as e:
        print(f"Index Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
