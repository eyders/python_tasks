"""
Module: test_word_builder
This module contains unit tests for the `construct_new_word` function.
"""

import unittest
from src.word_builder import construct_new_word


class TestWordBuilder(unittest.TestCase):
    """
    Unit tests for the word builder function.
    """

    def test_construct_word(self):
        """
        Tests constructing a word from specific letters of a list of words.
        """
        words = ['yoda', 'best', 'has']
        self.assertEqual(construct_new_word(words), 'yes')

    def test_empty_list(self):
        """
        Tests constructing a word from an empty list.
        """
        words = []
        self.assertEqual(construct_new_word(words), None)


if __name__ == '__main__':
    unittest.main()
