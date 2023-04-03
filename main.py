"""
<<<<<<< Updated upstream
CSC111 Course Project: SkinGenius: Your Personalized Skincare Matchmaker
This file is Copyright (c) 2023 Vivian Feng, Cailyn Kim, Jainam Shah, and Jennifer Tan.
<<<<<<< HEAD

This is the main file of the function that initiates and runs the complete simulation.
=======
=======
CSC111 Course Project: Skincare Recommender
Vivian Feng, Cailyn Kim, Jainam Shah, Jennifer Tan
>>>>>>> a63a806151ea0b93cac14cc041ffc418083113f4
"""
from intialize import read_csv
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
    network.filter(budget, product, skin_type, brand)


if __name__ == '__main__':
    runner()
