"""
CSC111 Course Project: SkinGenius: Your Personalized Skincare Matchmaker
This file is Copyright (c) 2023 Vivian Feng, Cailyn Kim, Jainam Shah, and Jennifer Tan.
The intial dataset of the program is extracted here and placed into the program graph
"""

import os
import csv

from network import Network, Product, User, Review


def read_csv() -> Network:
    """ This function extracts intiail data from the dataset in csv file and adds them to the network"""

    network = Network()

    directory = 'data/reviews'
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

            new_product = Product(address=product_address, name=name, brand=brand, price=price, category=category)

            network.add_node(new_product)

            product_address += 1

        product_nodes = network.get_product_nodes

        all_url = []
        for product in reader_product:
            all_url.append(product[10])

        # address accumulator assigned here, so it will accumulate for every review of every file
        user_address = 0

        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            with open(file_path, encoding="utf8") as file:

                p_id = str(filename)
                p_id = p_id.replace(".csv", "?")

                for i in range(len(all_url)):
                    if p_id == all_url[i]:
                        # this product (its review file) is found in product info csv (by search for p_id in url)
                        # the current row contains the file product
                        # now read each review (one per row)
                        curr_product = product_nodes[i]

                        reader_review = csv.reader(filename)
                        next(reader_product)

                        for review in reader_review:
                            name = review[0]
                            curr_user = User(user_address, name)
                            skin_type = review[3]
                            rating = float(review[1])
                            # adds user to graph within add_review
                            # product suitability also updated within
                            network.add_review(user=curr_user, product=curr_product, rating=(skin_type, rating))

                            user_address += 1

    return network
