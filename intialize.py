import os
import csv

directory = 'data/reviews'
with open('data/sample_products.csv', encoding="utf8") as products:
    reader_product = csv.reader(products)
    row1 = next(reader_product)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        with open(file_path, encoding="utf8") as file:

            p_id = str(filename)
            p_id = p_id.replace(".csv", "?")

            for row in reader_product:
                url = row[10]
                if p_id in url:
                    print(url)
