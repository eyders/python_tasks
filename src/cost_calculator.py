"""
Module: cost_calculator
This module provides a function to calculate the total cost of items with tax.
"""


def get_total(costs, items_bought, tax_rate):
    """
    Calculates the total cost of items purchased, including tax.

    Args:
        costs (dict): A dictionary of items and their costs (key: item name, value: price).
        items_bought (list): A list of items purchased.
        tax_rate (float): The tax rate as a decimal (0.09 for 9%).

    Returns:
        float: The total cost including tax, rounded to two decimals.
    """
    try:
        total = sum(costs[item] for item in items_bought if item in costs)
        total_with_tax = total + (total * tax_rate)
        return round(total_with_tax, 2)
    except KeyError:
        print('Error: One or more items not found in the costs dictionary.')
        return None
    except TypeError:
        print('Error: Invalid input types. Ensure costs is a dictionary, items_bought is a list, and tax_rate is a number.')
        return None
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None
