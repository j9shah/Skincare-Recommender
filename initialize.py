"""
CSC111 Course Project: Sephora Beauty Matchmaker
This file is Copyright (c) 2023 Vivian Feng, Cailyn Kim, Jainam Shah, and Jennifer Tan.
The intial dataset of the program is extracted here and placed into the program graph
"""

import os
import csv

from network import Product, User
from recommendation import RecommenderGraph

brands = []
categories = []


def read_csv() -> RecommenderGraph:
    """ This function extracts intiail data from the dataset in csv file and adds them to the network"""

    network = RecommenderGraph()

    with open('data/sample_products.csv', encoding="utf8") as products:
        reader_product = csv.reader(products)
        next(reader_product)

        # create Product object

        product_address = 0
        for row in reader_product:

            name = row[3]
            brand = row[1]
            price = float(row[8])
            category = row[2]
            print(category)

            new_product = Product(address=product_address, name=name, brand=brand, price=price, category=category)

            network.add_node(new_product)

            product_address += 1

        brands.extend(network.get_brands())
        categories.extend(network.get_category())
        product_nodes = network.get_product_nodes()

        all_url = []
        for product in reader_product:
            all_url.append(product[10])

        # address accumulator assigned here, so it will accumulate for every review of every file
        user_address = 0

        match_reviews(all_url, product_nodes, user_address, network)

    return network


def match_reviews(all_url: list, product_nodes: dict, user_address: int, network: RecommenderGraph) -> None:
    """ Matches review file's corresponding product with exisitng product. """
    directory = 'data/reviews'
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        p_id = str(filename)
        p_id = p_id.replace(".csv", "?")

        for i in range(len(all_url)):
            if p_id in all_url[i]:
                # this product (its review file) is found in product info csv (by search for p_id in url)
                # the current row contains the file product
                # now read each review (one per row)
                curr_product = product_nodes[i]

                user_address += insert_reviews(file_path, curr_product, user_address, network)


def insert_reviews(file_path: str, curr_product: Product, user_address: int, network: RecommenderGraph) -> int:
    """ Creates a review for every row of the review file (a single review) and add to network. """
    with open(file_path, encoding="utf8") as file:

        reader_review = csv.reader(file)
        next(reader_review)

        for review in reader_review:
            name = review[0]
            curr_user = User(user_address, name)
            skin_type = review[3]
            rating = float(review[1])
            # adds user to graph within add_review
            # product suitability also updated within
            network.add_review(user=curr_user, product=curr_product, rating=(skin_type, rating))

            user_address += 1

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
