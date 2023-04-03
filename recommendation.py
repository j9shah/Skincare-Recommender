"""
CSC111 Course Project: SkinGenius: Your Personalized Skincare Matchmaker
This file is Copyright (c) 2023 Vivian Feng, Cailyn Kim, Jainam Shah, and Jennifer Tan.
recommendation program that recommends the user of a product depending on the skin type they have
"""
from typing import Optional

import network


class RecommenderGraph(network.Network):
    """
        Abstract Recommender object that will recommend items depending on the preference of the user.
    """
    # def __init__(self, reviews: list[network.Review]) -> None:
    #     for review in reviews:
    #         product = review.get_product()
    #         user = review.get_user()
    #         self.add_review(user, product, review.rating)
    #         # self._nodes[product].update_suitability()

    def filter(self, budget: int, product: str, skin_type: str, brand: Optional[str]) -> list[network.Product]:
        """Returns a list of filtered products

        The list will first sort by how suitable the product is for a skin type, and then by price.

        If there are no products for the specific category, the program will return a list of products from most popular
        to least popular.

        """
        new_products = []
        products = self.get_product_nodes()
        for node in products:
            if self._products[node].price <= budget and self._products[node].category == product:
                if brand is not None and brand == self._products[node].brand:
                    new_products.append(self._products[node])
                else:
                    new_products.append(self._products[node])
        new_products.sort(key=lambda x: x.suitability[skin_type])
        new_products.sort(key=lambda x: x.price)

        if not new_products:
            for node in products:
                new_products.append(self._products[node])
            new_products.sort(key=lambda x: len(x.reviews))

        return new_products
