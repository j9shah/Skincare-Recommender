"""recommendation program that recommends the user of a product depending on the skin type they have"""
import network

class AbstractRecommender(network.Network):
    """Abstract Recommender object that will recommend items depending on the preference of the user."""
    def __init__(self):
        super().__init__()

    def find_paths(self):
        """Returns a list of paths from one Product to Another"""

def similar_items():
    """Returns a list of items with similar reviews and skin type and price in the order of how similar they are

    First, it looks for most similar in terms of skin type
    If there are ties, put the one with a lower price first

    If there is a tie again with the prices, go in alphabetical order of the name of the product.

    Implementation:

    """
