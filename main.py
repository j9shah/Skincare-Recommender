"""
CSC111 Course Project: Sephora Beauty Matchmaker
This file is Copyright (c) 2023 Vivian Feng, Cailyn Kim, Jainam Shah, and Jennifer Tan.

This is the main file of the function that initiates and runs the complete simulation.
"""
from initialize import read_csv
import simulation


def runner() -> None:
    """
    Runs all methods needed in order to return an output
    """
    # Loading in csv files
    network = read_csv()

    # Getting input from user
    product = simulation.get_category_input()
    skin_type = simulation.get_skin_type_input()
    budget = simulation.get_budget_input()
    brand = simulation.get_brand_input()

    # performing computations on the data
    recommended_products = network.filter(budget, product, skin_type, brand)

    # returning output
    simulation.get_output(recommended_products)


if __name__ == '__main__':
    runner()

    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'extra-imports': ['initialize', 'simulation'],
    })
