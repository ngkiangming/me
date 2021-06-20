# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""


import math

# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.

    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}

    This will be quite hard, especially hard if you don't have a good diagram!

    Use the VS Code debugging tools a lot here. It'll make understanding
    things much easier.
    """
    tries = 0
    guess = 0
    number = list(range(low, high + 1))
    middle = (low + high) // 2
    if number[middle] == actual_number:
        tries = tries + 1
        guess = actual_number
    else:
        while guess != actual_number:
            if number[middle] == actual_number:
                guess = actual_number
            elif number[middle] > actual_number:
                tries = tries + 1
                high = middle
                middle = (low + high) // 2
            elif number[middle] < actual_number:
                tries = tries + 1
                low = middle
                middle = (low + high) // 2
    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
    print(binary_search(0, 100, 50))
