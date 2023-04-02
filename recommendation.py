"""recommendation program that recommends the user of a product depending on the skin type they have"""
import network

class AbstractRecommender(network.Network):
    """Abstract Recommender object that will recommend items depending on the preference of the user."""
    def __init__(self):
        super().__init__()
        self.brand_list = brand_list #need to fix this
        self.skin_type_list = skin_type_list #need to fix this
        self.price_range_list = price_range_list #need to fix this

    def find_paths(self):
        """Returns a list of paths from one Product to Another"""
        recommended_products = self.recommend_products(self.brand_list, self.skin_type_list, self.price_range_list)

        # Return these products
        return recommended_products

    def recommend_products(self, brand_list, skin_type_list, price_range_list):
        """Returns a list of products that match the given brand, skin type, and price range, sorted by ratings"""
        brand_products = set(brand_list)
        skin_type_products = set(skin_type_list)
        price_range_products = set(price_range_list)

        # Get the set of products that appear in all 3 lists
        recommended_products = brand_products.intersection(skin_type_products, price_range_products)

        # Sort the recommended products by their ratings
        sorted_products = sorted(recommended_products, key=lambda x: float(x.split(",")[5]), reverse=True)

        return sorted_products
