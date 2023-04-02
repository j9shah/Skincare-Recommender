"""recommendation program that recommends the user of a product depending on the skin type they have"""
import network


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
        """Return a set of products that match the given product type, skin type, brand, and price range, sorted by
        ratings
        """
        product_set = set(tuple(p) for p in self.product_dict.values()) & set(
            tuple(s) for s in self.skin_type_dict.values()) & set(tuple(b) for b in self.brand_dict.values()) & set(
            tuple(p) for p in self.price_range_dict.values())

        unique_products = []
        for product in product_set:
            if product not in unique_products:
                unique_products.append(product)

        sorted_products = sorted(unique_products, key=lambda x: x[5], reverse=True)

        return sorted_products
