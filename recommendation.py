"""recommendation program that recommends the user of a product depending on the skin type they have"""
from typing import Optional

import network

class RecommenderGraph(network.Network):
    """
        Abstract Recommender object that will recommend items depending on the preference of the user.
    """
    def __init__(self, reviews: list[network.Review]) -> None:
        for review in reviews:
            product = review.get_product()
            user = review.get_user()
            self.add_review(user, product, review.rating)
            # self._nodes[product].update_suitability()

    def filter_by_budget(self, budget: int, product: str, skin_type) -> Optional[list[network.Node]]:
        """Returns a list of filtered products"""
        new_products = []
        products = self.get_product_nodes()
        for node in products:
            if self._products[node].price <= budget:
                if self._product
                new_products.append(self._products[node])
        new_products.sort(key=lambda x: x.price)
        return new_products



class AbstractRecommender(network.Network):
    """
    Abstract Recommender object that will recommend items depending on the preference of the user.
    """
    def __init__(self, product_dict, skin_type_dict, brand_dict, price_range_dict):
        super().__init__()
        self.product_dict = product_dict
        self.skin_type_dict = skin_type_dict
        self.brand_dict = brand_dict
        self.price_range_dict = price_range_dict

    def recommend_products(self):
        """Return a list of products that match the given product type, skin type, brand, and price range, sorted by
        ratings
        """
        # Check that all dictionaries are non-empty
        if not all((self.product_dict, self.skin_type_dict, self.brand_dict, self.price_range_dict)):
            return []

        # Get the lists of products from the dictionaries
        product_type = self.product_dict.values()
        product_type1 = list(product_type)[0]

        skin_type = self.skin_type_dict.values()
        skin_type1 = list(skin_type)[0]

        brand = self.brand_dict.values()
        brand1 = list(brand)[0]

        price_range = self.price_range_dict.values()
        price_range1 = list(price_range)[0]

        # Get the intersection of the four lists
        recommended_products = set(
            set(product_type1) & set(skin_type1) & set(brand1) & set(price_range1))

        recommended_products_list = list(recommended_products)

        # Sort the list by rating, highest to lowest
        recommended_products_list.sort(key=lambda x: x['rating'], reverse=True)

        return recommended_products
