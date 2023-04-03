""" The intial dataset of the program is extracted here and placed into the program graph"""

import os
import csv

from network import Network, Product, User, Review


def read_csv() -> Network:
    """ This function extracts intiail data from the dataset in csv file and adds them to the network"""

    network = Network()

    directory = 'data/reviews'
    with open('data/sample_products.csv', encoding="utf8") as products:
        reader_product = csv.reader(products)
        row1 = next(reader_product)

        # create Product object

        i = 0
        for row in reader_product:

            address = i
            name = row[3]
            brand = row[1]
            price = float(row[8])
            category = row[2]

            new_product = Product(address=address, name=name, brand=brand, price=price, category=category)

            network.add_node(new_product)

            i += 1

        product_nodes = network.get_product_nodes

        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            with open(file_path, encoding="utf8") as file:

                p_id = str(filename)
                p_id = p_id.replace(".csv", "?")

                for product in reader_product:
                    url = product[10]
                    if p_id in url:
                        print(url)  # placeholder
                        # this product (its review file) is found in product info csv (by search for p_id in url)
                        # the current row contains the file product
                        # now read each review (one per row)

                        reader_review = csv.reader(filename)
                        row1 = next(reader_product)
                        i = 0
                        for review in reader_review:
                            address = i
                            name = review[0]

                            curr_product = product_nodes[address]
                            curr_user = User(address, name)
                            skin_type = review[3]
                            rating = float(review[1])
                            # adds user to graph within add_review
                            network.add_review(curr_user, curr_product, (skin_type, rating))

                            # update suitability attribute
                            curr_product.update_suitability()   # needing the Review we just made in parameter

    return network
