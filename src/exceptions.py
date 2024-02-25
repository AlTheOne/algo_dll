class NodeAlreadyExistException(Exception):
    """Node already exists at node_map"""


class NodeDoesNotExistException(Exception):
    """Node does not exists at node_map"""


class InvalidNextIdException(Exception):
    """Invalid next id"""
