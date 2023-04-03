"""
CSC111 Course Project: SkinGenius: Your Personalized Skincare Matchmaker
This file is Copyright (c) 2023 Vivian Feng, Cailyn Kim, Jainam Shah, and Jennifer Tan.

This is the main file of the function that initiates and runs the complete simulation.
"""
from intialize import read_csv
import simulation

def runnner() -> None:
    """ Calls for dataset initialization """
    network = read_csv()

if __name__ == '__main__':
    # Loading in csv files
    # Getting input from user
    product = simulation.get_category_input()
    skin_type = simulation.get_skin_type_input()
    budget = simulation.get_budget_input()
    brand = simulation.get_brand_input()


    # performing computations on the data
