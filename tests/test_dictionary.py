"""
Module: test_dictionary
This module contains unit tests for the Dictionary class.
"""

import unittest
from src.dictionary import Dictionary


class TestDictionary(unittest.TestCase):
    """
    Unit tests for the Dictionary class.
    """

    def test_new_entry_and_lookup(self):
        """
        Tests adding a new entry to the dictionary and looking it up.
        """
        d = Dictionary()
        d.newentry('Apple', 'A fruit that grows on trees')
        self.assertEqual(d.look('Apple'), 'A fruit that grows on trees')

    def test_lookup_non_existent_word(self):
        """
        Tests looking up a word that does not exist in the dictionary.
        """
        d = Dictionary()
        self.assertEqual(d.look('Banana'), "Can't find entry for Banana")


if __name__ == '__main__':
    unittest.main()
