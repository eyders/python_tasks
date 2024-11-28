"""
Module: dictionary
This module defines the Dictionary class, which provides methods to add words 
and retrieve their definitions.
"""


class Dictionary:
    """
    A class that implements a custom dictionary to store words and their definitions.
    """

    def __init__(self):
        """
        Initializes the dictionary with an empty data store.
        """
        self.data = {}

    def newentry(self, key, value):
        """
        Adds a new word and its definition to the dictionary.

        Args:
            key (str): The word to add.
            value (str): The definition of the word.
        """

        try:
            self.data[key] = value
        except (TypeError, ValueError) as e:
            print(f'Error adding entry: {e}')
            return None

    def look(self, key):
        """
        Looks up a word in the dictionary and returns its definition.

        Args:
            key (str): The word to look up.

        Returns:
            str: The definition of the word, or a message if the word is not found.
        """
        try:
            return self.data.get(key, f"Can't find entry for {key}")
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            return None
