"""
CSC111 Course Project: Sephora Beauty Matchmaker
This file is Copyright (c) 2023 Vivian Feng, Cailyn Kim, Jainam Shah, and Jennifer Tan.
The initial dataset of the program is extracted here and placed into the program graph
"""

import os
import csv

from network import Product, User
from recommendation import RecommenderGraph

# delcare global variable to assign a list of all product brands and categories, and later pass to simulation.py
brands = []
categories = []


def read_csv() -> RecommenderGraph:
    """ This function extracts intiail data from the dataset in csv file and adds them to the network"""
    # initialize graph
    network = RecommenderGraph()

    # open sample products and skip first row (headers)
    with open('data/sample_products.csv', encoding="utf8") as products:
        reader_product = csv.reader(products)
        next(reader_product)

        # declare an accumulator for address
        product_address = 0
        # each row is a product, so create a Product object from information in each row
        for row in reader_product:
            # collected object attributes
            name = row[3]
            brand = row[1]
            price = float(row[8])
            category = row[2]
            # create new Product object and add to network
            new_product = Product(address=product_address, name=name, brand=brand, price=price, category=category)
            network.add_node(new_product)
            # update accumulator
            product_address += 1

        # collect all brands and catgories of product in network, now that all are initialized
        brands.extend(network.get_brands())
        categories.extend(network.get_category())
        # store dictionary of address to products from current network
        product_nodes = network.get_product_nodes()

        # store all product url for matching review to product in match_reviews
        all_url = []
        for product in reader_product:
            all_url.append(product[10])

        # address accumulator assigned here, so it will accumulate for every review of every file
        user_address = 0
        # call match_reviews to initialize all reviews from sample dataset
        match_reviews(all_url, product_nodes, user_address, network)

    return network


def match_reviews(all_url: list, product_nodes: dict, user_address: int, network: RecommenderGraph) -> None:
    """ Matches review file's corresponding product with exisitng product. """
    # loop through each review files in "reviews" folder
    directory = 'data/reviews'
    for filename in os.listdir(directory):
        # store complete file dirctory for use in insert_reviews
        file_path = os.path.join(directory, filename)
        # store filename as product id
        p_id = str(filename)
        p_id = p_id.replace(".csv", "?")
        # loop through all product url and find product id within url
        for i in range(len(all_url)):
            # if product id found in current url, the prodcut this file reviews in found in current network
            if p_id in all_url[i]:
                # due to how product address was assigned previously,
                # the current index of the url is the products' address in the network
                curr_product = product_nodes[i]
                # call insert_reviews to initilize all reviews and accumulate user_address
                user_address += insert_reviews(file_path, curr_product, user_address, network)


def insert_reviews(file_path: str, curr_product: Product, user_address: int, network: RecommenderGraph) -> int:
    """ Creates a review for every row of the review file (a single review) and add to network. """
    # the current file has reviews with an existing product in network
    with open(file_path, encoding="utf8") as file:
        reader_review = csv.reader(file)
        next(reader_review)
        # extract each row (each is one review) and create a Review object
        for review in reader_review:
            # store object attributes
            name = review[0]
            curr_user = User(user_address, name)
            skin_type = review[3]
            rating = float(review[1])
            # use add_review to creat a new Review obejct and add to network
            # User object (node) is also added to graph within add_review
            network.add_review(user=curr_user, product=curr_product, rating=(skin_type, rating))
            # update accumulator
            user_address += 1
    # return address accumulator for continue use in extracting the next review file
    return user_address


def pass_brands_list() -> list[str]:
    """
    This function is a helper for simulation.py. It passes the list of brands of the products in the network.
    """
    return brands


def pass_category_list() -> list[str]:
    """
    This function is a helper for simulation.py. It passes the list of categories of the products in the network.
    """
    return categories


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'extra-imports': ['os', 'csv', 'network', 'recommendation'],
        'allowed-io': ['read_csv', 'insert_reviews'],
        'disable': ['E9992', 'E9997']
    })
