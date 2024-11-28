"""
Main entry point for running tasks in the Docker container.
This script reads environment variables and executes the corresponding task.
"""

import os
from dictionary import Dictionary
from cost_calculator import get_total
from word_builder import construct_new_word


def main():
    """Python Tasks"""
    task = os.getenv('TASK', 'dictionary')

    if task == 'dictionary':
        print('Running Dictionary Task...')
        key = os.getenv('WORD', 'Apple')
        value = os.getenv('DEFINITION', 'A fruit that grows on trees')
        d = Dictionary()
        d.newentry(key, value)
        print(d.look(key))
        print(d.look('Banana'))
    elif task == 'cost_calculator':
        print('Running Cost Calculator Task...')
        costs = {'socks': 5, 'shoes': 60, 'sweater': 30}
        items = os.getenv("ITEMS", "socks,shoes").split(',')
        tax = float(os.getenv('TAX', 0.09))
        total = get_total(costs, items, tax)
        print(f'Total cost with tax: {total}')
    elif task == "word_builder":
        print('Running Word Builder Task...')
        words = os.getenv('WORDS', 'yoda,best,has').split(',')
        result = construct_new_word(words)
        print(f'Constructed word: {result}')
    else:
        print("Invalid TASK specified. Use 'dictionary', 'cost_calculator', or 'word_builder'.")


if __name__ == "__main__":
    main()
