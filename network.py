"""The main network of the program is created here as well its various nodes and edges."""

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
    address = NodeAddress
    reviews = dict[NodeAddress, Review]

    def __int__(self, address: NodeAddress) -> None:
        """Initialize this node with the given address and no current connections to other nodes."""
        self.address = address
        self.channels = {}


class User(Node):
    """A user node that represents individual users in a network

    Instance Attributes:
    - name:
        the name of the user to that is displayed when showing reccomendations
    """
    name = str

    def __int__(self, name: str) -> None:
        """Initialize this node with the given address and no current connections to other nodes."""
        super().__init__()
        self.name = name


class Product(Node):
    """A user node that represents individual users in a network

        Instance Attributes:
        - name:
            the name of the product to that is displayed when showing reccomendations
    """
    name = str
    brand = str
    price = int
    def __int__(self, name: str) -> None:
        """Initialize this node with the given address and no current connections to other nodes."""
        super().__init__()
        self.name = name


class Review:
    """A user node that represents individual users in a network

        Instance Attributes:
        - endpoints:
           the nodes that are connected together by the review
        - ratings:
            a mapping of reviews types. The keys correspond to the skin type and the rating corresponds to the review
            given for that product and skin type.
    """
    endpoints = set[Node]
    ratings = dict[str, float]

    def __init__(self, n1: Node, n2: Node, rating: tuple[str, float]) -> None:
        self.endpoints = {n1, n2}
        self.ratings[rating[0]] = rating[1]


class Network:
    """The network that contains the information of the skincare recommender

    Private Instance Attributes:
    - _nodes:
        the nodes that are within the network

    """
    _nodes: dict[NodeAddress, Node]

    def __init__(self) -> None:
        self._nodes = {}

    def add_node(self, address: NodeAddress) -> Node:
        """Addes a node to the network and returns it"""
        new_node = Node(address)
        self._nodes[address] = new_node
        return new_node

    def add_review(self, n1: NodeAddress, n2: NodeAddress, rating: tuple[str, float]) -> None:
        """Makes a review between two nodes"""
        if n1 not in self._nodes:
            self.add_node(n1)
        if n2 not in self._nodes:
            self.add_node(n2)

        Review(self._nodes[n1], self._nodes[n2], rating)
