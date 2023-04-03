"""The main network of the program is created here as well its various nodes and edges."""
from __future__ import annotations

NodeAddress = int | str

class Node:
    """A node that represents a user or product in a network.

    Instance Attributes:
    - address:
        the address in which a user or product is identified by. There are two types, number addresses (user) and
        letter addresses (product)
    - reviews:
        A mapping containing the reviews which are like the edges of the graph and represent the connection between a
        user and a product. Each key represents the other nodes that are connected to the current node.
    """
    address: NodeAddress
    reviews: dict[NodeAddress, Review]

    def __init__(self, address: NodeAddress) -> None:
        """Initialize this node with the given address and no current connections to other nodes."""
        self.address = address
        self.reviews = {}


class User(Node):
    """A user node that represents individual users in a network

    Instance Attributes:
    - name:
        the name of the user to that is displayed when showing reccomendations
    """
    name: str
    skin_type: str

    def __init__(self, address: NodeAddress, name: str) -> None:
        """Initialize this node with the given address and no current connections to other nodes."""
        super().__init__(address)
        self.name = name


class Product(Node):
    """A user node that represents individual users in a network

    Instance Attributes:
    - name:
        the name of the product to that is displayed when showing reccomendations
    - brand:
        the name of the brand of the product that is displayed when filtering

    """
    name: str
    brand: str
    price: float
    category: str
    suitability: dict[str, float]

    def __init__(self, address: NodeAddress, name: str, brand: str, price: float, category: str) -> None:
        """Initialize this node with the given address and no current connections to other nodes."""
        super().__init__(address)
        self.name = name
        self.brand = brand
        self.price = price
        self.category = category
        self.suitability = {'oily': 0.0, 'dry': 0.0, 'combination': 0.0, 'average': 0.0}

    def update_suitability(self, review: Review) -> None:
        """updates the suitability of a product"""
        new_average = (self.suitability[review.rating[0]]*len(self.reviews) + review.rating[1]) / (len(self.reviews)+1)
        self.suitability[review.rating[0]] = new_average


class Review:
    """A user node that represents individual users in a network

    Instance Attributes:
    - endpoints:
       the nodes that are connected together by the review
    - ratings:
        the rating given to the product

    """
    endpoints: set[Node]
    rating: tuple[str, float]

    def __init__(self, n1: Node, n2: Node, rating: tuple[str, float]) -> None:
        self.endpoints = {n1, n2}
        # self.ratings['oily'] = 0.0
        # self.ratings['dry'] = 0.0
        # self.ratings['combination'] = 0.0
        # self.ratings['average'] = 0.0
        # updates rating
        self.rating = rating

    def get_product(self):
        """returns the product node of the endpoint"""
        for point in self.endpoints:
            if isinstance(point.address, int):
                return point

    def get_user(self):
        """returns the user node of the endpoint"""
        for point in self.endpoints:
            if not isinstance(point.address, int):
                return point


class Network:
    """The network that contains the information of the skincare recommender

    Private Instance Attributes:
    - _nodes:
        the nodes that are within the network

    """
    _users: dict[NodeAddress, User]
    _products: dict[NodeAddress, Product]

    def __init__(self) -> None:
        self._users = {}
        self._products = {}

    def add_node(self, node: User | Product) -> Node:
        """Addes a node to the network and returns it"""
        if node.address % 2 == 0:
            self._users[node.address] = node
        else:
            self._products[node.address] = node
        return node

    def add_review(self, user: User, product: Product, rating: tuple[str, float]) -> None:
        """Makes a review between two nodes"""
        if user.address not in self._users:
            self.add_node(user)
        if product.address not in self._users:
            self.add_node(product)

        Review(self._users[user.address], self._users[product.address], rating)
        review = self._products[product.address].reviews[user.address]
        self._products[product.address].update_suitability(review)

    def get_nodes(self) -> dict[NodeAddress, Node]:
        """Returns the current nodes in the network"""
        return self._users

    def get_product_nodes(self) -> dict[NodeAddress, Product]:
        """Returns the current product nodes in the network"""
        return self._products

    def get_user_nodes(self) -> dict[NodeAddress, User]:
        """Returns the current user nodes in the network"""
        return self._users
