import pytest

from src.manager import DllManager
from src.nodes import Node

__all__ = [
    'dll_manager_filled',
    'dll_manager_empty',
    'dll_manager_with_single_node',
]


@pytest.fixture
def dll_manager_filled() -> DllManager:
    node1 = Node(node_id=1)
    node2 = Node(node_id=2)
    node3 = Node(node_id=3)

    node1.next_node = node2

    node2.prev_node = node1
    node2.next_node = node3

    node3.prev_node = node2

    dll_manager = DllManager()
    dll_manager.node_map = {
        1: node1,
        2: node2,
        3: node3,
    }

    return dll_manager


@pytest.fixture
def dll_manager_empty() -> DllManager:
    return DllManager()


@pytest.fixture
def dll_manager_with_single_node() -> DllManager:
    node1 = Node(node_id=1)

    dll_manager = DllManager()
    dll_manager.node_map = {
        1: node1,
    }

    return dll_manager
