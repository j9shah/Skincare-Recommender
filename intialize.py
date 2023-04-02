""" The intial dataset of the program is extracted here and placed into the program graph"""

import os
import csv

from network import Product, User, Review

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

        new_product = Product(address, name, brand, price)    # need to add to the whole graph

        i += 1

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
                        curr_product = graph._nodes[address]    # need access graph nodes
                        curr_user = User(address, name)     # need to add to the whole graph
                        skin_type = review[3]
                        rating = float(review[1])
                        Review(curr_product, curr_user, (skin_type, rating))

                        # left to do: update suitability attribute
