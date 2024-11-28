"""
Module: test_cost_calculator
This module contains unit tests for the `get_total` function.
"""

import unittest
from src.cost_calculator import get_total


class TestCostCalculator(unittest.TestCase):
    """
    Unit tests for the cost calculator function.
    """

    def test_calculate_total_with_tax(self):
        """
        Tests calculating the total cost with tax.
        """
        costs = {'socks': 5, 'shoes': 60, 'sweater': 30}
        self.assertEqual(get_total(costs, ['socks', 'shoes'], 0.09), 70.85)

    def test_ignore_nonexistent_items(self):
        """
        Tests ignoring items that do not exist in the costs dictionary.
        """
        costs = {'socks': 5, 'shoes': 60}
        self.assertEqual(get_total(costs, ['socks', 'hat'], 0.05), 5.25)


if __name__ == '__main__':
    unittest.main()
